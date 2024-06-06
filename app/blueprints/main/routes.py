import logging
from flask import Flask, jsonify, request, Blueprint

from app.dto import parse_text_dto
from app.dto.world_dto import WorldDto
from app.services.world_service import WorldService
from app.utils.codes import get_code
from app.utils.custom_response import CustomResponse

success_output = [
    {
        "simpleText": {"text": "안녕 hello I'm Ryan"},
    }
]

fail_output = [
    {
        "simpleText": {"text": "test"},
    }
]


main = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@main.route("/", methods=["GET"])
def health_check():
    return {"status": "ok"}, 200


@main.route("/create", methods=["POST"])
def create_wolrd():
    body = request.get_json()
    # 딕셔너리를 클래스 인스턴스로 변환
    userRequest = body["userRequest"]
    bot_id = body["bot"]["id"]

    content = body["action"]["params"]["content"]
    user = userRequest["user"]["id"]
    code = get_code("0002")
    if content == None:
        return CustomResponse.simpleText(code)

    parse = parse_text_dto(content)
    if parse == None:
        return CustomResponse.simpleText(code)

    parse["chat_id"] = user
    parse["bot_id"] = bot_id

    # 세계 등록
    return WorldService.add_world(parse)


@main.route("/query", methods=["POST"])
def query_wolrd():
    body = request.get_json()
    bot_id = body["bot"]["id"]

    code = get_code("0002")

    if bot_id == None:
        return CustomResponse.simpleText(code)

    # 세계 등록
    return WorldService.query_world_with_user(bot_id)
