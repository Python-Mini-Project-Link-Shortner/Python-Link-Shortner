from flask              import render_template, Blueprint, redirect, request, jsonify
from backend.service    import url_service
import json

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/', defaults={'path': ''})
@main_controller.route('/<path:path>')
def home(path):
    # Root 페이지로 사용할 파일을 지정한다.
    return render_template('index.html')

@main_controller.route('/<short_url>')
def redirect_url(short_url):
    # 축약된 URL이 들어오면 DB에서 찾아 원본 링크로 연결한다.
    raw_url = url_service.get_url(short_url, target="raw")

    # 페이지가 존재하지 않으면 오류 페이지 출력
    if raw_url is None:
        return "Page Not Found"

    # HTTP로부터 통계정보 추출
    stats = url_service.get_stats_info(short_url)
    if stats is None: stats = {}
    url_service.extract_stats(request.environ, stats)

    # 통계정보 저장
    url_service.upsert_stats(short_url, stats)

    return redirect(raw_url)