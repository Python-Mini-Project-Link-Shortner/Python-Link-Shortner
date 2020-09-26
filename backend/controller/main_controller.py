from flask import render_template, Blueprint

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/', defaults={'path': ''})
@main_controller.route('/<path:path>')
def home(path):
    # Root 페이지로 사용할 파일을 지정한다.
    return render_template('index.html')