import datetime
import jwt  # Make sure to import the jwt module
from django.conf import settings  # Import settings to access SECRET_KEY

def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5),  # 5 minutes expiration
        'iat': datetime.datetime.now(datetime.timezone.utc)
    }
    access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7),  # Corrected from day to days
        'iat': datetime.datetime.now(datetime.timezone.utc)
    }
    refresh_token = jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')
    return refresh_token
