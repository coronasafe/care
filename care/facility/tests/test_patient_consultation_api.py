import datetime

from django.test import TestCase
from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from care.facility.api.viewsets.facility_users import FacilityUserViewSet
from care.facility.api.viewsets.patient_consultation import PatientConsultationViewSet
from care.facility.models.facility import Facility
from care.facility.models.patient_consultation import (
    CATEGORY_CHOICES,
    PatientConsultation,
)
from care.facility.tests.mixins import TestClassMixin
from care.users.models import Skill
from care.utils.tests.test_base import TestBase


class FacilityUserTest(TestClassMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.creator = self.users[0]

        sample_data = {
            "name": "Hospital X",
            "ward": self.creator.ward,
            "local_body": self.creator.local_body,
            "district": self.creator.district,
            "state": self.creator.state,
            "facility_type": 1,
            "address": "Nearby",
            "pincode": 390024,
            "features": [],
        }
        self.facility = Facility.objects.create(
            external_id="550e8400-e29b-41d4-a716-446655440000",
            created_by=self.creator,
            **sample_data,
        )

        self.skill1 = Skill.objects.create(name="Skill 1")
        self.skill2 = Skill.objects.create(name="Skill 2")

        self.users[0].skills.add(self.skill1, self.skill2)

    def test_get_queryset_with_prefetching(self):
        response = self.new_request(
            (f"/api/v1/facility/{self.facility.external_id}/get_users/",),
            {"get": "list"},
            FacilityUserViewSet,
            self.users[0],
            {"facility_external_id": self.facility.external_id},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNumQueries(2)


class TestPatientConsultation(TestBase, TestClassMixin, APITestCase):
    default_data = {
        "symptoms": [1],
        "category": CATEGORY_CHOICES[0][0],
        "examination_details": "examination_details",
        "history_of_present_illness": "history_of_present_illness",
        "prescribed_medication": "prescribed_medication",
        "suggestion": PatientConsultation.SUGGESTION_CHOICES[0][0],
    }

    def setUp(self):
        self.factory = APIRequestFactory()
        self.consultation = self.create_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )

    def create_admission_consultation(self, patient=None, **kwargs):
        patient = patient or self.create_patient(facility_id=self.facility.id)
        data = self.default_data.copy()
        kwargs.update(
            {
                "patient": patient.external_id,
                "facility": self.facility.external_id,
            }
        )
        data.update(kwargs)
        res = self.new_request(
            (self.get_url(), data, "json"),
            {"post": "create"},
            PatientConsultationViewSet,
            self.state_admin,
            {},
        )
        return PatientConsultation.objects.get(external_id=res.data["id"])

    def get_url(self, consultation=None):
        if consultation:
            return f"/api/v1/consultation/{consultation.external_id}"
        return "/api/v1/consultation"

    def discharge(self, consultation, **kwargs):
        return self.new_request(
            (f"{self.get_url(consultation)}/discharge_patient", kwargs, "json"),
            {"post": "discharge_patient"},
            PatientConsultationViewSet,
            self.state_admin,
            {"external_id": consultation.external_id},
        )

    def test_discharge_as_recovered_preadmission(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REC",
            discharge_date="2002-04-01T16:30:00Z",
            discharge_notes="Discharge as recovered before admission",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_discharge_as_recovered_future(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REC",
            discharge_date="2319-04-01T15:30:00Z",
            discharge_notes="Discharge as recovered in the future",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_discharge_as_recovered_after_admission(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REC",
            discharge_date="2020-04-02T15:30:00Z",
            discharge_notes="Discharge as recovered after admission before future",
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_discharge_as_expired_pre_admission(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="EXP",
            death_datetime="2002-04-01T16:30:00Z",
            discharge_notes="Death before admission",
            death_confirmed_doctor="Dr. Test",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_discharge_as_expired_future(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="EXP",
            death_datetime="2319-04-01T15:30:00Z",
            discharge_notes="Death in the future",
            death_confirmed_doctor="Dr. Test",
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_discharge_as_expired_after_admission(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="EXP",
            death_datetime="2020-04-02T15:30:00Z",
            discharge_notes="Death after admission before future",
            death_confirmed_doctor="Dr. Test",
            discharge_date="2319-04-01T15:30:00Z",
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_referred_to_external_null(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REF",
            discharge_date="2023-07-01T12:00:00Z",
            discharge_notes="Discharged with null referred_to_external",
            referred_to_external=None,
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_referred_to_external_empty_string(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REF",
            discharge_date="2023-07-01T12:00:00Z",
            discharge_notes="Discharged with empty referred_to_external",
            referred_to_external="",
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_referred_to_empty_facility(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REF",
            discharge_date="2023-07-01T12:00:00Z",
            discharge_notes="Discharged with empty referred_to_external",
            referred_to=None,
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_referred_to_and_external_together(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        res = self.discharge(
            consultation,
            discharge_reason="REF",
            discharge_date="2023-07-01T12:00:00Z",
            discharge_notes="Discharged with null referred_to_external",
            referred_to_external="External Facility",
            referred_to=self.facility.external_id,
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_referred_to_valid_value(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        referred_to_external = "Test Hospital"
        res = self.discharge(
            consultation,
            discharge_reason="REF",
            discharge_date="2023-07-01T12:00:00Z",
            referred_to_external=referred_to_external,
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_referred_to_external_valid_value(self):
        consultation = self.create_admission_consultation(
            suggestion="A",
            admission_date=make_aware(datetime.datetime(2020, 4, 1, 15, 30, 00)),
        )
        referred_to_external = "Test Hospital"
        res = self.discharge(
            consultation,
            discharge_reason="REF",
            discharge_date="2023-07-01T12:00:00Z",
            discharge_notes="Discharged with valid referred_to_external",
            referred_to_external=referred_to_external,
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
