from django.utils.timezone import datetime
from rest_framework import status
from rest_framework.test import APITestCase

from care.facility.models import Asset, Bed
from care.utils.tests.test_utils import TestUtils


class AssetViewSetTestCase(TestUtils, APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.state = cls.create_state()
        cls.district = cls.create_district(cls.state)
        cls.local_body = cls.create_local_body(cls.district)
        cls.super_user = cls.create_super_user("su", cls.district)
        cls.facility = cls.create_facility(cls.super_user, cls.district, cls.local_body)
        cls.asset_location = cls.create_asset_location(cls.facility)
        cls.user = cls.create_user("staff", cls.district, home_facility=cls.facility)
        cls.patient = cls.create_patient(
            cls.district,
            cls.facility,
            local_body=cls.local_body,
        )

    def setUp(self) -> None:
        super().setUp()
        self.asset = self.create_asset(self.asset_location)

    def test_list_assets(self):
        response = self.client.get("/api/v1/asset/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_asset(self):
        sample_data = {
            "name": "Test Asset",
            "current_location": self.asset_location.pk,
            "asset_type": 50,
            "location": self.asset_location.external_id,
        }
        response = self.client.post("/api/v1/asset/", sample_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_asset_with_warranty_past(self):
        sample_data = {
            "name": "Test Asset",
            "current_location": self.asset_location.pk,
            "asset_type": 50,
            "location": self.asset_location.external_id,
            "warranty_amc_end_of_validity": "2000-04-01",
        }
        response = self.client.post("/api/v1/asset/", sample_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_asset(self):
        response = self.client.get(f"/api/v1/asset/{self.asset.external_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_asset(self):
        sample_data = {
            "name": "Updated Test Asset",
            "current_location": self.asset_location.pk,
            "asset_type": 50,
            "location": self.asset_location.external_id,
        }
        response = self.client.patch(
            f"/api/v1/asset/{self.asset.external_id}/",
            sample_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], sample_data["name"])
        self.asset.refresh_from_db()
        self.assertEqual(self.asset.name, sample_data["name"])

    def test_update_asset_change_warranty_improperly(self):
        sample_data = {
            "warranty_amc_end_of_validity": "2002-04-01",
        }
        response = self.client.patch(
            f"/api/v1/asset/{self.asset.external_id}/",
            sample_data,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_asset_change_warranty_properly(self):
        sample_data = {
            "warranty_amc_end_of_validity": "2222-04-01",
        }
        response = self.client.patch(
            f"/api/v1/asset/{self.asset.external_id}/",
            sample_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_asset_failure(self):
        response = self.client.delete(f"/api/v1/asset/{self.asset.external_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Asset.objects.filter(pk=self.asset.pk).exists(), True)

    def test_delete_asset(self):
        user = self.create_user(
            "distadmin",
            self.district,
            home_facility=self.facility,
            user_type=30,
        )
        self.client.force_authenticate(user=user)
        response = self.client.delete(
            f"/api/v1/asset/{self.asset.external_id}/",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Asset.objects.filter(pk=self.asset.pk).exists(), False)

    def test_asset_filter_in_use_by_consultation(self):
        asset1 = Asset.objects.create(
            name="asset1",
            current_location=self.asset1_location,
        )
        asset2 = Asset.objects.create(
            name="asset2",
            current_location=self.asset1_location,
        )

        consultation = self.create_consultation(self.patient, self.facility)
        bed = Bed.objects.create(
            name="bed1",
            location=self.asset1_location,
            facility=self.facility,
        )
        self.client.post(
            "/api/v1/consultationbed/",
            {
                "consultation": consultation.external_id,
                "bed": bed.external_id,
                "start_date": datetime.now().isoformat(),
                "assets": [asset1.external_id, asset2.external_id],
            },
        )

        response = self.client.get("/api/v1/asset/?in_use_by_consultation=true")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

        response = self.client.get("/api/v1/asset/?in_use_by_consultation=false")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
