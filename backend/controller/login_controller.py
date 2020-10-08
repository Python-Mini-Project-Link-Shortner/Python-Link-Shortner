from flask              import Blueprint, session, request, jsonify
from backend.service    import user_service
from datetime           import datetime

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