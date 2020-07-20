from handling_db import MongoDB
from handling_url import create_short_url, validate_url
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
Mongo = MongoDB()

@app.route('/')
def home():
    # Root 페이지로 사용할 파일을 지정한다.
    # HTML은 서버 파일(flask)과 인접한 'templates' 폴더에 있어야 함.
    return render_template('index.html')

@app.route('/ajax', methods=['GET', 'POST'])
def shorten_url():
    # AJAX를 통해 원본 URL을 처리하는 페이지.

    # 원본 URL 데이터 가져오기
    raw_url = request.form['raw_url']
    if not validate_url(raw_url):
        return "Invalid URL"

    # 이미 저장된 URL인지 확인
    short_url = Mongo.get_short_url(raw_url)

    # 새로운 URL 일경우
    if short_url is None:
        print("raw_url is not in db")

        # 짧은 URL 생성
        unique_id = Mongo.get_unique_id()
        short_url = create_short_url(unique_id)

        # DB에 추가
        db_data = {
            'Raw_URL': raw_url,
            'Short_URL': short_url
        }
        Mongo.save_data(db_data)

        # DB 추가 후 unique_id를 증가시킨다.
        Mongo.increase_id()

        print("raw_url: ", raw_url, " short_url: ", short_url)

    # AJAX에 축약된 URL을 반환한다.
    return request.host_url + short_url

@app.route('/<short_url>')
def redirect_url(short_url):
    # 축약된 URL이 들어오면 DB에서 찾아 원본 링크로 연결한다.
    Raw_URL = Mongo.get_URL({'Short_URL': short_url})     # 샘플 코드, 확인 후 삭제할 것.

    # 페이지가 존재하지 않으면 오류 페이지 출력
    if Raw_URL is None:
        return render_template('page_404.html')

    return redirect(Raw_URL)

if __name__ == "__main__":
    app.run(debug=True)