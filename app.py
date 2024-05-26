import debugpy
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)

# debugpy.listen(("0.0.0.0", 5678))
# print("Debugger is listening on port 5678")
# debugpy.wait_for_client()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy 초기화
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)


# 데이터베이스 초기화 (첫 실행 시)
with app.app_context():
    db.create_all()


@app.route("/", methods=["POST"])
def index():
    body = request.get_json()
    print(body)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {"text": "안녕 hello I'm Ryan"},
                },
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Ryan",
                    }
                },
            ]
        },
    }

    return responseBody


@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message_text = data.get("message")
    response_text = f"You said: {message_text}"

    return jsonify({"response": response_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
