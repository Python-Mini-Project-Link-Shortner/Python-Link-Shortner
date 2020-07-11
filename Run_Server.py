from handling_db import MongoDB
from handling_url import make_it_short
from flask import Flask, render_template, url_for, request
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

    # URL을 축약하는 부분
    raw_url = request.get_data()
    short_url = make_it_short(raw_url)

    # DB에 넣는 부분
    db_data = {
        'Raw_URL': raw_url,
        'Short_URL': short_url
    }
    Mongo.save_data(db_data)

    return short_url

if __name__ == "__main__":
    app.run(debug=True)