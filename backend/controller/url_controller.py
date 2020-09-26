from flask              import Blueprint, request, jsonify
from backend.service    import url_service

url_controller = Blueprint('url_controller', __name__)

@app.route('shorten', methods=['GET', 'POST'])
def shorten_url():
    # 원본 URL 데이터 가져오기
    req_data = request.get_json()
    raw_url = req_data['url']

    # 반환 변수 설정
    res_data = {'flag': True}

    # URL 형식이 올바르지 않으면 False 반환
    if not url_service.validate_url(raw_url):
        res_data['flag'] = False
        res_data['msg'] = 'Invalid URL'
        return jsonify(res_data)

    # 프로토콜이 생략된 url을 수정한다.
    raw_url = normalize_url(raw_url)

    # 이미 저장된 URL인지 확인
    short_url = Mongo.get_short_url(raw_url)

    # 새로운 URL 일경우
    if short_url is None:
        # 짧은 URL 생성
        unique_id = Mongo.get_unique_id()
        short_url = create_short_url(unique_id)

        # DB에 추가
        db_data = {
            'rawURL': raw_url,
            'shortURL': short_url
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

    # 축약된 URL을 반환한다.
    return jsonify({
        'flag': True,
        'msg': request.host_url + short_url
        })

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