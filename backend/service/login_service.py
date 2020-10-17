import os
# Google OAuth
from apiclient          import discovery
from oauth2client       import client

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', None)
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', None)

def handshake_oauth(code):

    # 일회성 코드와 Access 토큰, Refresh 토큰 교환
    credentials = client.credentials_from_code(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        ['profile', 'email'],
        code
    )

    # 이메일과 아이디 받기
    user_id = credentials.id_token['sub']
    email = credentials.id_token['email']

    # TODO: refresh 토큰 저장, 결과값 반환, frontend >> account.js 완성