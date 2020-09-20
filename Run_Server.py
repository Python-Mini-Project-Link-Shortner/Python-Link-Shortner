from handling_db import MongoDB
from handling_url import create_short_url, validate_url, normalize_url
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_cors import CORS
from data_encoder import DataEncoder

app = Flask(__name__,
            static_folder='static',
            template_folder = "templates")
Mongo = MongoDB()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# 미식별 링크에 대한 기본 홈. (path는 슬래시를 포함한 str)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    # Root 페이지로 사용할 파일을 지정한다.
    return render_template('index.html')

@app.route('/api/shorten', methods=['GET', 'POST'])
def shorten_url():
    # AJAX를 통해 원본 URL을 처리하는 페이지.

    # 원본 URL 데이터 가져오기
    raw_url = request.json['url']
    if not validate_url(raw_url):
        return jsonify({
            'flag': False,
            'msg': 'Invalid URL.'
        })

    # 프로토콜이 생략된 url을 수정한다.
    raw_url = normalize_url(raw_url)

    # 이미 저장된 URL인지 확인
    short_url = Mongo.get_short_url(raw_url)

    # 새로운 URL 일경우
    if short_url is None:
        print("raw_url is not in db, It's free to go.")

        # 짧은 URL 생성
        unique_id = Mongo.get_unique_id()
        short_url = create_short_url(unique_id)

        # DB에 추가
        db_data = {
            'Raw_URL': raw_url,
            'Short_URL': short_url
        }
        flag = Mongo.save_data(db_data, 'LINKS')

        # DB 추가 후 unique_id를 증가시킨다.
        if flag:
            Mongo.increase_id()
        else:
            return jsonify({
                'flag': False,
                'msg': 'DB save failed.'
            })

        print("raw_url: ", raw_url, " short_url: ", short_url)

    # AJAX에 축약된 URL을 반환한다.
    return jsonify({
        'flag': True,
        'msg': request.host_url + short_url
        })

# 신규유저 등록 및 로그인 시간을 갱신하는 페이지 (로그인 시)
@app.route('/api/login', methods=['GET','POST'])
def update_user():
    # 유저 정보 가져오기
    email = request.json['email']
    id_token = request.json['idToken']

    # 유저를 검색한다.
    user_info = Mongo.find_data({'email': email},'USERS')

    # 신규 유저인 경우 추가
    if user_info is None:
        Mongo.upsert_user(id_token, email)
        return jsonify({'flag': True})

    # 정지되지 않은 정상 유저인 경우 로그인시간 갱신
    banned = user_info['banned']
    if not banned:
        Mongo.upsert_user(id_token, email)
        return jsonify({'flag': True})
    # 정지 됐을경우
    else:
        return jsonify({'flag': False, 'msg': 'This user is banned'})

    # 나머지 경우
    return jsonify({'flag':True})

# 축약된 URL의 원본 URL을 반환하는 페이지
@app.route('/api/check', methods=['GET', 'POST'])
def check_url():
    short_url = request.json['url']
    
    # 축약 링크를 DB에서 검색한다.
    raw_url = Mongo.get_raw_url(short_url)

    # 링크가 존재하지 않으면 실패 반환
    if raw_url is None:
        return jsonify({
            'flag': False,
            'msg': "The link provided doesn't exist."
        })
    
    return jsonify({
        'flag': True,
        'link': raw_url
    })

@app.route('/<short_url>')
def redirect_url(short_url):
    # 축약된 URL이 들어오면 DB에서 찾아 원본 링크로 연결한다.
    Raw_URL = Mongo.get_raw_url(short_url)

    # 페이지가 존재하지 않으면 오류 페이지 출력
    if Raw_URL is None:
        return "Page Not Found"

    return redirect(Raw_URL)

@app.route('/api/linkList', methods=['POST'])
def link_list():
    req_data = request.get_json()

    user_id = req_data['user_id']
    page = req_data['page']
    item_count = req_data['item_count']

    res = Mongo.get_link_pagination(user_id, page, item_count)
    if res is None: return None

    # pagination 가능하게 pagination.py 작성
    # page, maxPage, list Dictionary로 반환하게
    return DataEncoder().encode(res)

@app.route('/api/deleteLink', methods=['POST'])
def delete_link():
    req_data = request.get_json()

    user_id = req_data['user_id']
    item_list = req_data['delete_id']

    delete_all = True
    for id in item_list:
        res = Mongo.delete_link(user_id, id)
        if res == False: delete_all = False
        # TODO :
        # 나중에 res가 false이면 MongoDB가 transaction 지원 없으므로 SQL 전부 저장해서 원복시켜야 합니다
        # 기술 지원 따로 있음. 찾아보기.

    if delete_all is True: return jsonify({ 'Flag': True })
    return jsonify({ 'Flag': False })

if __name__ == "__main__":
    print(app.root_path)
    print(app.static_folder)
    print(app.static_url_path)
    print(app._static_folder)
    app.run(debug=True)