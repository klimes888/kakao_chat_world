from flask import jsonify
from app.utils import codes


class CustomResponse:
    @staticmethod
    def simpleText(text=""):

        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {"text": text},
                    }
                ]
            },
        }
        return jsonify(responseBody)

    @staticmethod
    def simpleImage(outputs=[]):
        responseBody = {
            "version": "2.0",
            "template": {"outputs": outputs},
        }
        return jsonify(responseBody)


#   {
#       "simpleImage": {
#           "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
#           "altText": "hello I'm Ryan",
#       }
#   },
