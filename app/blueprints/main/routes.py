import logging
from flask import Flask, jsonify, request, Blueprint

main = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@main.route("/", methods=["GET"])
def health_check():
    return {"status": "ok"}, 200


@main.route("/", methods=["POST"])
def index():
    body = request.get_json()
    # logger.info(body)
    print(f"test: {body}")
    return "test!"
