from flask              import Blueprint, request, jsonify
from backend.service    import url_service

url_controller = Blueprint('url_controller', __name__)

@url_controller.route('shorten', methods=['GET', 'POST'])
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

    # 축약 URL을 등록한다.
    short_url = url_service.register_url(raw_url)
    if short_url == False:
        # 저장에 실패한 경우
        res_data['flag'] = False
        res_data['msg']  = 'DB save failed'
        return jsonify(res_data)

    print("raw_url: ", raw_url, " short_url: ", short_url)

    res_data['flag'] = True
    res_data['msg']  = request.host_url + short_url
    return jsonify(res_data)

# 축약된 URL의 원본 URL을 반환하는 페이지
@url_controller.route('/api/check', methods=['GET', 'POST'])
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