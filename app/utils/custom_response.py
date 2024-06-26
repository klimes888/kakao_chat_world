from flask import jsonify
from app.utils import codes


class CustomResponse:
    @staticmethod
    def text_with_img(text="", img_url=""):

        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": img_url,
                            "altText": "img_url",
                        },
                    },
                    {
                        "simpleText": {"text": text},
                    },
                ]
            },
        }
        return jsonify(responseBody)

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
