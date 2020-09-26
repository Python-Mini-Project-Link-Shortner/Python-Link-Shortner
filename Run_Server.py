from flask import Flask, render_template, url_for, request, redirect, jsonify, Blueprint
from flask_cors import CORS
from whitenoise import WhiteNoise
from backend.controller.main_controller import main_controller
from backend.controller.login_controller import login_controller

from backend.handling_db import MongoDB
from backend.handling_url import create_short_url, validate_url, normalize_url
from backend.database.util.data_encoder import DataEncoder

app = Flask(__name__, template_folder='frontend\dist', static_folder='frontend\dist')
app.wsgi_app = WhiteNoise(app.wsgi_app, root='frontend', prefix='dist')
app.json_encoder = DataEncoder # Encoder change to Custom Encoder
CORS(app, resources={r'/*': {'origins': '*'}}) # enable CORS

# Register Blueprints
# https://flask.palletsprojects.com/en/1.1.x/blueprints/
app.register_blueprint(main_controller)

# DB 따로 만들기
Mongo = MongoDB()

if __name__ == "__main__":
    print(app.root_path)
    print(app.static_folder)
    print(app.static_url_path)
    print(app._static_folder)
    app.run(debug=True)