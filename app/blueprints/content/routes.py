import logging
from flask import Flask, jsonify, request, Blueprint

from app.dto import parse_text_dto
from app.utils.codes import get_code
from app.services.country_service import CountryService
from app.utils.custom_response import CustomResponse


content = Blueprint("content", __name__)
logger = logging.getLogger(__name__)


@content.route("/country", methods=["POST"])
def create_country():
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
    return CountryService.add_country(parse)
