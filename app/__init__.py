from flask import Flask
from .extensions import db, migrate
from .blueprints.main.routes import main


def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    # 확장 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트 등록
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
