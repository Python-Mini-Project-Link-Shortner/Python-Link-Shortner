from flask import Blueprint, session, request, jsonify
from backend.service import user_service

login_controller = Blueprint('login_controller', __name__)

# 신규유저 등록 및 로그인 시간을 갱신하는 페이지 (로그인 시)
@login_controller.route('/login', methods=['GET','POST'])
def update_user():
    # 클라이언트가 보낸 유저 정보 가져오기
    req_data = request.get_json()
    email = req_data['email']
    id_token = req_data['idToken']

    # TODO: Login Time과 Create Time 나누고, 아이디가 있는지 없는지 구분해서 데이턴 넣어주고
    # ban 상태일 때 데이터 구분해서 넣어줘야한다
    res_data = { 'flag': True }
    if not user_service.is_normal_user(email):
        res_data['flag'] = False
        res_data['msg'] = 'This user is banned'
        return jsonify(res_data)

    user_service.upsert_user(email, id_token)
    return jsonify(res_data)