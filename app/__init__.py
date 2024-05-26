from dotenv import load_dotenv
from flask import Flask
from .extensions import db, migrate
from .blueprints.main.routes import main
import os

# 환경 변수 로드


def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 확장 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트 등록
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
