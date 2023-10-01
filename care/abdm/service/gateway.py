import uuid
from datetime import datetime, timezone

from django.conf import settings

from care.abdm.models.base import Purpose
from care.abdm.models.consent import ConsentRequest
from care.abdm.service.request import Request


class Gateway:
    def __init__(self):
        self.request = Request(settings.ABDM_URL + "/gateway")

    def consent_requests__init(self, consent: ConsentRequest):
        data = {
            "requestId": str(consent.external_id),
            "timestamp": datetime.now(tz=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"
            ),
            "consent": {
                "purpose": {
                    "text": Purpose(consent.purpose).label,
                    "code": Purpose(consent.purpose).value,
                },
                "patient": {"id": consent.patient_abha.health_id},
                "hiu": {
                    "id": "IN3210000017"
                },  # TODO: get the HIU ID associated with the patient's facility
                "requester": {
                    "name": f"{consent.requester.REVERSE_TYPE_MAP[consent.requester.user_type]}, {consent.requester.first_name} {consent.requester.last_name}",
                    "identifier": {
                        "type": "Care Username",
                        "value": consent.requester.username,
                        "system": settings.CURRENT_DOMAIN,
                    },
                },
                "hiTypes": consent.hi_types,
                "permission": {
                    "accessMode": consent.access_mode,
                    "dateRange": {
                        "from": consent.from_time.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                        "to": consent.to_time.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                    },
                    "dataEraseAt": consent.expiry.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                    "frequency": {
                        "unit": consent.frequency_unit,
                        "value": consent.frequency_value,
                        "repeats": consent.frequency_repeats,
                    },
                },
            },
        }

        path = "/v0.5/consent-requests/init"
        return self.request.post(path, data, headers={"X-CM-ID": settings.X_CM_ID})

    def consent_requests__status(self, consent_request_id: str):
        data = {
            "requestId": str(uuid.uuid4()),
            "timestamp": datetime.now(tz=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"
            ),
            "consentRequestId": consent_request_id,
        }

        return self.request.post(
            "/v0.5/consent-requests/status", data, headers={"X-CM-ID": settings.X_CM_ID}
        )

    def consents__fetch(self, consent_artefact_id: str):
        data = {
            "requestId": str(uuid.uuid4()),
            "timestamp": datetime.now(tz=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"
            ),
            "consentId": consent_artefact_id,
        }

        return self.request.post(
            "/v0.5/consents/fetch", data, headers={"X-CM-ID": settings.X_CM_ID}
        )
