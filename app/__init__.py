import os
from dotenv import load_dotenv
from flask import Flask
from .extensions import db, migrate
from .blueprints.main.routes import main
from .blueprints.user.routes import user
import logging

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "secretkey1111")


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # 확장 초기화

    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트 등록
    app.register_blueprint(main)
    app.register_blueprint(user)

    # 로그 설정
    logging.basicConfig(level=logging.INFO)

    with app.app_context():
        db.create_all()

    return app


from app import models
