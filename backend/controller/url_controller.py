from flask              import Blueprint, request, jsonify, redirect
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

    # 이미 저장된 URL인지 확인
    raw_url = url_service.normalize_url(raw_url)
    short_url = url_service.get_url(raw_url, target="short")

    # 축약 URL을 등록한다.
    if short_url == None:
        short_url = url_service.register_url(raw_url)

    # URL 등록에 실패한 경우
    if short_url == None:
        res_data['flag'] = False
        res_data['msg']  = 'DB save failed'
        return jsonify(res_data)

    print("raw_url: ", raw_url, " short_url: ", short_url)

    res_data['flag'] = True
    res_data['msg']  = request.host_url + short_url
    return jsonify(res_data)

# 축약된 URL의 원본 URL을 반환하는 페이지
@url_controller.route('check', methods=['GET', 'POST'])
def check_url():
    req_data = request.get_json()
    res_data = { 'flag': True }
    
    # 축약 링크를 DB에서 검색한다.
    short_url = req_data['url']
    raw_url = url_service.get_url(short_url, target="raw")

    # 링크가 존재하지 않으면 실패 반환
    if raw_url is None:
        res_data['flag'] = False
        res_data['msg']  = "The link provided doesn't exist."
        return jsonify(res_data)
    
    res_data['flag'] = True
    res_data['link'] = raw_url
    return jsonify(res_data)

@url_controller.route('/<short_url>')
def redirect_url(short_url):
    # 축약된 URL이 들어오면 DB에서 찾아 원본 링크로 연결한다.
    raw_url = url_service.get_url(short_url)

    # 페이지가 존재하지 않으면 오류 페이지 출력
    if raw_url is None:
        return "Page Not Found"

    return redirect(raw_url)