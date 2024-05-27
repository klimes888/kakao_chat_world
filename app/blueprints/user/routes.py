import logging
from flask import Flask, jsonify, request, Blueprint
from app.services.user_service import UserService

user = Blueprint("user", __name__, url_prefix="/user")
logger = logging.getLogger(__name__)


@user.route("/create", methods=["POST"])
def index():
    body = request.get_json()
    user_data = body["data"]
    user = UserService.add_user(user_data)
    logger.info(user)
    return {"result": "ok"}, 200
