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
    print('Acess Token: ', credentials.access_token)
    print('Refresh Token: ', credentials.refresh_token)
    print('ID Token: ', credentials.id_token)

    # TODO: refresh 토큰 저장, 결과값 반환, frontend >> account.js 완성