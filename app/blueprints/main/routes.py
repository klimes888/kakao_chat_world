import logging
from flask import Flask, jsonify, request, Blueprint

from app.dto import parse_text_dto
from app.dto.world_dto import WorldDto
from app.services.world_service import WorldService
from app.utils.custom_response import CustomResponse

main = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@main.route("/", methods=["GET"])
def health_check():
    return {"status": "ok"}, 200


@main.route("/world", methods=["POST"])
def index():
    body = request.get_json()
    # 딕셔너리를 클래스 인스턴스로 변환
    userRequest = body["userRequest"]
    utterance = userRequest["utterance"]
    user = userRequest["user"]["id"]
    # input_data = WorldDto(InputData, utterance)

    parse = parse_text_dto(utterance)

    success_output = [
        {
            "simpleText": {"text": "안녕 hello I'm Ryan"},
        }
    ]

    fail_output = [
        {
            "simpleText": {
                "text": "세계를 등록하기 위해서는\n다음과 같이 입력해주세요\n이미지가 없으면 빈값으로 둬주세요\n/세계등록 [이름='', 설명='', 이미지='']\n\nex. /세계등록 [이름=신세계, 설명=좋은 곳, 이미지=www.exam.com/image.jpg]"
            },
        }
    ]

    if parse == None:
        return CustomResponse.simpleText("0001", fail_output)

    # parse["user_id"] = user
    parse["bot_id"] = "test1234"

    # 세계 등록
    world = WorldService.add_world(parse)

    return CustomResponse.simpleText("0000", success_output)
