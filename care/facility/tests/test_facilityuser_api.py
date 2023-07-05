from django.test import TestCase

from care.facility.api.viewsets.facility_users import FacilityUserViewSet
from care.facility.models.facility import Facility
from care.facility.tests.mixins import TestClassMixin
from care.users.models import Skill


class FacilityUserTest(TestClassMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.creator = self.users[0]

        # Create Facility
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

        # Create Skills
        self.skill1 = Skill.objects.create(name="Skill 1")
        self.skill2 = Skill.objects.create(name="Skill 2")

        # Assign Skills to Users
        self.users[0].skills.add(self.skill1, self.skill2)

    def test_get_queryset_with_prefetching(self):
        response = self.new_request(
            (f"/api/v1/facility/{self.facility.external_id}/get_users/",),
            {"get": "list"},
            FacilityUserViewSet,
            self.users[0],
            {"facility_external_id": self.facility.external_id},
        )

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        # Assert the database queries
        self.assertNumQueries(2)  # 1 for user and 1 user for skills
