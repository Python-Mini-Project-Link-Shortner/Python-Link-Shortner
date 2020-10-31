# Standard Libraries
from datetime           import datetime
from os                 import abort
import smtplib, ssl
# Third Party Libraries
from flask              import Blueprint, session, request, jsonify
# Custom Modules
from backend.service    import user_service, minipy_service

minipy_controller = Blueprint('minipy_controller', __name__)

# 신규유저 등록 및 로그인 시간을 갱신하는 페이지 (로그인 시)
@minipy_controller.route('/login', methods=['GET','POST'])
def update_user():
    # 인증코드로부터 토큰 얻기
    req_data = request.get_json()
    auth_code = req_data['code']
    user_data = minipy_service.handshake_oauth(auth_code)
    
    # 구글에서 얻은 유저 정보
    email = user_data['email']
    name = user_data['name']
    expiresAt = user_data['expiresAt']
    access_token = user_data['accessToken']
    refresh_token = user_data['refreshToken']

    # 반환값 및 갱신 정보
    res_data = {
        'flag': True,
        'email': email,
        'name': name,
        'expiresAt': expiresAt
        }
    update_data = { 
        'lastAccess': datetime.now(),
        'accessToken': access_token,
        'refreshToken': refresh_token
        }
    user_info = user_service.get_user_info(email)

    # 정지된 유저인 경우
    if user_info['banned']:
        res_data['flag'] = False
        res_data['msg'] = 'This user is banned'
    # 일반 유저인 경우
    else:
        res_data['flag'] = True
        update_data['lastLogin'] = datetime.now()

    # 업데이트 후 종료
    user_service.upsert_user(email, update_data)
    return jsonify(res_data)


# 불만, 피드백 등을 받아 이메일로 전송하는 페이지
@minipy_controller.route('/contact', methods=['GET','POST'])
def send_email():
    # 반환값
    res_data = {'flag': True}

    # 폼 데이터 정리
    req_data = request.get_json()
    name = req_data['name']
    email = req_data['email']
    subject = req_data['subject']
    message = req_data['message']

    # 메일 전송용 텍스트
    text = f"Subject: [MiniPy] {subject} \n\n"
    text += f"Name: {name}\n"
    text += f"Message: {message}"
    text = text.encode('utf-8')     # 한글도 보낼 수 있게 하기 위함.

    # 메일 전송
    flag = minipy_service.send_gmail(email, text)
    res_data['flag'] = flag

    return jsonify(res_data)