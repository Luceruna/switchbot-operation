import os
import time
import hashlib
import hmac
import base64
import uuid
import dotenv
from typing import Dict
dotenv.load_dotenv()


def create_sign() -> Dict[str, str]:
    token = os.getenv('TOKEN')
    secret = bytes(os.getenv('SECRET'), 'utf-8')
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = bytes(f'{token}{t}{nonce}', 'utf-8')

    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    return {
        'Authorization': token,
        'Content-Type': 'application/json',
        'charset': 'utf8',
        't': str(t),
        'sign': sign,
        'nonce': str(nonce)
    }
