from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    body = request.get_json()
    print(body)
    app.logger.debug(f"test ---------<{body['userRequest']}")

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {"text": "안녕 hello I'm Ryan"},
                },
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Ryan",
                    }
                },
            ]
        },
    }

    return responseBody


@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message_text = data.get("message")
    response_text = f"You said: {message_text}"

    return jsonify({"response": response_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
