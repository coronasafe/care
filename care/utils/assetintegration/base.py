import enum
import json

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.exceptions import APIException, PermissionDenied

from care.users.models import User
from care.utils.jwks.token_generator import generate_jwt


class BaseAssetIntegration:
    auth_header_type = "Care_Bearer "

    class BaseAssetActions(enum.Enum):
        UNLOCK_ASSET = "unlock_camera"
        LOCK_ASSET = "lock_camera"
        REQUEST_ACCESS = "request_access"

    def __init__(self, meta):
        self.meta = meta
        self.host = self.meta["local_ip_address"]
        self.middleware_hostname = self.meta["middleware_hostname"]
        self.insecure_connection = self.meta.get("insecure_connection", False)

    def get_url(self, endpoint):
        protocol = "http"
        if not self.insecure_connection or settings.IS_PRODUCTION:
            protocol += "s"
        return f"{protocol}://{self.middleware_hostname}/{endpoint}"

    def api_post(self, url, data=None):
        req = requests.post(
            url,
            json=data,
            headers={"Authorization": (self.auth_header_type + generate_jwt())},
        )
        try:
            response = req.json()
            if req.status_code >= 400:
                raise APIException(response, req.status_code)
            return response
        except json.decoder.JSONDecodeError:
            return {"error": "Invalid Response"}

    def api_get(self, url, data=None):
        req = requests.get(
            url,
            params=data,
            headers={"Authorization": (self.auth_header_type + generate_jwt())},
        )
        try:
            if req.status_code >= 400:
                raise APIException(req.text, req.status_code)
            response = req.json()
            return response
        except json.decoder.JSONDecodeError:
            return {"error": "Invalid Response"}

    def handle_action(self, action, **kwargs):
        raise NotImplementedError

    def validate_action(self, action):
        pass

    def generate_system_users(self, asset_id):
        asset_queue_key = f"waiting_queue_{asset_id}"
        if cache.get(asset_queue_key) is None:
            return []
        else:
            queue = cache.get(asset_queue_key)
            users_array = list(User.objects.filter(username__in=queue))
            return users_array

    def generate_notification(self, asset_id):
        from care.utils.notification_handler import send_webpush

        message = {
            "type": "MESSAGE",
            "asset_id": str(asset_id),
            "status": "success",
        }
        user_array = self.generate_system_users(asset_id)
        for username in user_array:
            send_webpush(username=username, message=json.dumps(message))

    def add_to_waiting_queue(self, username, asset_id):
        asset_queue_key = f"waiting_queue_{asset_id}"
        if cache.get(asset_queue_key) is None:
            cache.set(asset_queue_key, [username], timeout=None)
        else:
            queue = cache.get(asset_queue_key)
            if username not in queue:
                queue.append(username)
                cache.set(asset_queue_key, queue, timeout=None)

    def remove_from_waiting_queue(self, username, asset_id):
        asset_queue_key = f"waiting_queue_{asset_id}"
        if cache.get(asset_queue_key) is None:
            return
        else:
            queue = cache.get(asset_queue_key)
            if username in queue:
                queue = [x for x in queue if x != username]
            cache.set(asset_queue_key, queue, timeout=None)

    def raise_conflict(self, asset_id):
        asset_lock_key = f"asset_lock_{asset_id}"
        user: User = User.objects.get(username=cache.get(asset_lock_key))
        raise PermissionDenied(
            {
                "message": "Asset is currently in use by another user",
                "username": user.username,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "role": [x for x in User.TYPE_CHOICES if x[0] == user.user_type][0][1],
                "homeFacility": user.home_facility.name
                if (user.home_facility and user.home_facility.name)
                else "",
            }
        )

    def verify_access(self, username, asset_id):
        asset_lock_key = f"asset_lock_{asset_id}"
        if cache.get(asset_lock_key) is None or cache.get(asset_lock_key) == username:
            return True
        elif cache.get(asset_lock_key) != username:
            return False
        return True

    def request_access(self, username, asset_id):
        from care.utils.notification_handler import send_webpush

        asset_lock_key = f"asset_lock_{asset_id}"
        if cache.get(asset_lock_key) is None or cache.get(asset_lock_key) == username:
            return {}
        elif cache.get(asset_lock_key) != username:
            user: User = User.objects.get(username=username)
            message = {
                "type": "MESSAGE",
                "status": "request",
                "username": user.username,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "role": [x for x in User.TYPE_CHOICES if x[0] == user.user_type][0][1],
                "homeFacility": user.home_facility.name
                if (user.home_facility and user.home_facility.name)
                else "",
            }

            send_webpush(
                username=cache.get(asset_lock_key), message=json.dumps(message)
            )
            return {"message": "user notified"}
