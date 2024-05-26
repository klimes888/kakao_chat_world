from flask import Flask, jsonify, request, Blueprint

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def health_check():
    return {"status": "ok"}, 200


@main.route("/", methods=["POST"])
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
