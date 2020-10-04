from flask      import Flask
from whitenoise import WhiteNoise
from flask_cors import CORS

from backend.database.util.data_encoder     import DataEncoder
from backend.controller.main_controller     import main_controller
from backend.controller.login_controller    import login_controller
from backend.controller.url_controller      import url_controller
from backend.controller.manage_controller   import manage_controller

def create_app():
    app = Flask(__name__, 
        template_folder='frontend/dist',
    )

    # WhiteNoise 세팅
    app.wsgi_app = WhiteNoise(
        app.wsgi_app,
        root="frontend/dist/",           # 정적 파일을 찾을 폴더 경로
        prefix="dist/"          # 정적 파일 요청임을 구분할 URL 접두사
    )
    # 인코더 변경
    app.json_encoder = DataEncoder
    # 블루프린트 등록
    # https://flask.palletsprojects.com/en/1.1.x/blueprints/
    app.register_blueprint(main_controller)
    app.register_blueprint(login_controller, url_prefix="/api")
    app.register_blueprint(url_controller, url_prefix="/api")
    app.register_blueprint(manage_controller, url_prefix="/api")
    # CORS 세팅
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app