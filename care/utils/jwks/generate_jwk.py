import base64
import json

from authlib.jose import JsonWebKey


def generate_encoded_jwks():
    key = JsonWebKey.generate_key("RSA", 2048, is_private=True)
    key = key.as_dict(key.dumps_private_key(), alg="RS256")

    keys = {"keys": [key]}
    keys_json = json.dumps(keys)
    return base64.b64encode(keys_json.encode()).decode()
