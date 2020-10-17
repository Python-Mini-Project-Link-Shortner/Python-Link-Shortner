# Standard Libraries
from datetime           import datetime
from os                 import abort
# Third Party Libraries
from flask              import Blueprint, session, request, jsonify
# Custom Modules
from backend.service    import user_service, login_service

login_controller = Blueprint('login_controller', __name__)

# 신규유저 등록 및 로그인 시간을 갱신하는 페이지 (로그인 시)
@login_controller.route('/login', methods=['GET','POST'])
def update_user():
    # 클라이언트가 보낸 유저 정보 가져오기
    req_data = request.get_json()
    email = req_data['email']

    # 반환값 및 유저 정보
    res_data = { 'flag': True }
    update_data = { 'lastAccess': datetime.now() }
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

# Oauth 핸드쉐이크
@login_controller.route('/authCode', methods=['GET','POST'])
def oauth_shake():
    req_data = request.get_json()

    # X-Requested-With가 없는 경우 CSRF
    if not request.headers.get('X-Requested-With'):
        abort(403)

    # 일회성 코드와 Access 토큰, Refresh 토큰 교환
    login_service.handshake_oauth(req_data['code'])

    return {'flag': True}