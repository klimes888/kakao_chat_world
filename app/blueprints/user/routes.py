import logging
from flask import Flask, jsonify, request, Blueprint
from app.services.user_service import UserService
from app.utils.custom_response import CustomResponse

user = Blueprint("user", __name__)
logger = logging.getLogger(__name__)


@user.route("/create", methods=["POST"])
def index():
    body = request.get_json()
    # user_data = body["data"]
    # user = UserService.add_user(user_data)
    logger.info(f"body ----> {body}")
    output = [
        {
            "simpleText": {"text": "안녕 hello I'm Ryan"},
        }
    ]

    return CustomResponse.simpleText("0000", output)
