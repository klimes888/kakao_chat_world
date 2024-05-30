import logging
from flask import Flask, jsonify, request, Blueprint
from app.services.user_service import UserService

user = Blueprint("user", __name__)
logger = logging.getLogger(__name__)


@user.route("/create", methods=["POST"])
def index():
    body = request.get_json()
    # user_data = body["data"]
    # user = UserService.add_user(user_data)
    logger.info(f"body ----> {body}")
    return {"result": "ok"}, 200


# @main.route("/", methods=["POST"])
# def index():
#     body = request.get_json()
#     print(body)
#     # app.logger.debug(f"test ---------<{body['userRequest']}")

#     responseBody = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText": {"text": "안녕 hello I'm Ryan"},
#                 },
#                 {
#                     "simpleImage": {
#                         "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
#                         "altText": "hello I'm Ryan",
#                     }
#                 },
#             ]
#         },
#     }

#     return responseBody


# @main.route("/chatbot", methods=["POST"])
# def chatbot():
#     data = request.json
#     if not data or "message" not in data:
#         return jsonify({"error": "No message provided"}), 400

#     message_text = data.get("message")
#     response_text = f"You said: {message_text}"

#     return jsonify({"response": response_text})
