import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.now(datetime.timezone.utc)
    }
    access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS25')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload ={
        'user_id': user.id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(day=7),
        'iat': datetime.datetime.now(datetime.timezone.utc)
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256'
    )
    return refresh_token

