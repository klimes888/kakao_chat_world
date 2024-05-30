from flask import jsonify
from app.utils import codes


class CustomResponse:
    @staticmethod
    def success(code="0000", status=200, data=None):
        response = {
            "status": "success",
            "code": code,
            "message": codes[code],
            "data": data,
        }
        return jsonify(response), status

    @staticmethod
    def error(code="0001", status=500):
        response = {"status": "error", "code": code, "message": codes[code]}
        return jsonify(response), status
