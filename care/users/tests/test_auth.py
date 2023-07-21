from django.conf import settings
from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework import status

from care.utils.tests.test_base import TestBase


class TestAuthTokens(TestBase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        settings.DISABLE_RATELIMIT = True

    def test_login_with_valid_credentials(self):
        response = self.client.post(
            "/api/v1/auth/login/",
            {"username": "user", "password": "bar"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("refresh" in response.data)
        self.assertTrue("access" in response.data)

    def test_login_with_missing_fields(self):
        response = self.client.post(
            "/api/v1/auth/login/",
            {"username": self.user.username},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["password"][0], "This field is required.")

    def test_login_with_invalid_credentials(self):
        response = self.client.post(
            "/api/v1/auth/login/",
            {"username": "invalid", "password": "invalidpassword"},
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"],
            "No active account found with the given credentials",
        )

    def test_auth_refresh_with_valid_credentials(self):
        response = self.client.post(
            "/api/v1/auth/login/",
            {"username": "user", "password": "bar"},
        )
        refresh = response.data["refresh"]
        response = self.client.post(
            "/api/v1/auth/token/refresh/",
            {"refresh": refresh},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("refresh" in response.data)
        self.assertTrue("access" in response.data)

    def test_auth_refresh_with_missing_fields(self):
        response = self.client.post("/api/v1/auth/token/refresh/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["refresh"][0], "This field is required.")

    def test_auth_refresh_with_invalid_token(self):
        response = self.client.post(
            "/api/v1/auth/token/refresh/",
            {"refresh": "invalid"},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"], "Token is invalid or expired")

    def test_auth_verify(self):
        response = self.client.post(
            "/api/v1/auth/login/",
            {"username": "user", "password": "bar"},
        )
        access = response.data["access"]
        response = self.client.post(
            "/api/v1/auth/token/verify/",
            {"token": access},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_verify_with_missing_fields(self):
        response = self.client.post("/api/v1/auth/token/verify/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["token"][0], "This field is required.")

    def test_auth_verify_with_invalid_token(self):
        response = self.client.post("/api/v1/auth/token/verify/", {"token": "invalid"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"], "Token is invalid or expired")


class TestPasswordReset(TestBase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        settings.DISABLE_RATELIMIT = True

    def test_forgot_password_with_valid_input(self):
        response = self.client.post(
            "/api/v1/password_reset/",
            {"username": self.user.username},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(ResetPasswordToken.objects.filter(user=self.user).exists())

    def test_forgot_password_with_missing_fields(self):
        response = self.client.post("/api/v1/password_reset/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()["username"][0], "This field is required.")

    def test_forgot_password_with_invalid_username(self):
        response = self.client.post(
            "/api/v1/password_reset/",
            {"username": "invalid"},
        )
        # for security reasons, we don't want to reveal if the user exists or not
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forgot_password_with_inactive_user(self):
        user = self.create_user(username="test1", district=self.district)
        user.is_active = False
        user.save()
        response = self.client.post(
            "/api/v1/password_reset/",
            {"username": user.username},
        )
        # for security reasons, we don't want to reveal if the user exists or not
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.delete()

    def test_verify_password_reset_token(self):
        token = self.create_reset_password_token(user=self.user)
        response = self.client.post(
            "/api/v1/password_reset/check/",
            {"token": token.key, "email": self.user.email},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verify_password_reset_token_with_missing_fields(self):
        response = self.client.post("/api/v1/password_reset/check/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "The password reset link is invalid")

    def test_verify_password_reset_token_with_invalid_token(self):
        response = self.client.post(
            "/api/v1/password_reset/check/",
            {"token": "invalid_token", "email": "invalid@g.com"},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "The password reset link is invalid")

    def test_verify_password_reset_token_with_expired_token(self):
        token = self.create_reset_password_token(user=self.user, expired=True)
        response = self.client.post(
            "/api/v1/password_reset/check/",
            {"token": token.key, "email": self.user.email},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            response.data["detail"],
            "The password reset link has expired",
        )

    def test_reset_password_with_valid_token(self):
        token = self.create_reset_password_token(user=self.user)
        response = self.client.post(
            "/api/v1/password_reset/confirm/",
            {"token": token.key, "password": "test@123"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_password_with_missing_fields(self):
        response = self.client.post("/api/v1/password_reset/confirm/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()["token"][0], "This field is required.")
        self.assertEqual(response.json()["password"][0], "This field is required.")

    def test_reset_password_with_invalid_token(self):
        response = self.client.post(
            "/api/v1/password_reset/confirm/",
            {"token": "invalid_token", "password": "test@123"},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Not found.")

    def test_reset_password_with_expired_token(self):
        token = self.create_reset_password_token(user=self.user, expired=True)
        response = self.client.post(
            "/api/v1/password_reset/confirm/",
            {"token": token.key, "password": "test@123"},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Not found.")
