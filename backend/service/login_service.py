import os
# Google OAuth
from apiclient          import discovery
from oauth2client       import client

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', None)
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', None)
if GOOGLE_CLIENT_ID is None:
    raise Exception("환경변수 GOOGLE_CLIENT_ID를 설정해주십시오.")
if GOOGLE_CLIENT_SECRET is None:
    raise Exception("환경변수 GOOGLE_CLIENT_SECRET을 설정해주십시오.")

def handshake_oauth(code):

    # 일회성 코드와 Access 토큰, Refresh 토큰 교환
    credentials = client.credentials_from_code(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        ['profile', 'email'],
        code
    )

    # 이메일과 아이디 받기
    access_token = credentials.access_token
    refresh_token = credentials.refresh_token
    email = credentials.id_token['email']
    name = credentials.id_token['name']

    # 반환
    return {
        'accessToken': access_token,
        'refreshToken': refresh_token,
        'email': email,
        'name': name
    }