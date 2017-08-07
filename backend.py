from flask import Flask, request, abort
from linebot_commands import *

app = Flask(__name__)


@app.route("/", methods=['POST', "GET"])
def index():
    app.logger.info("test~~~~ logger")
    print("print~~~~~")
    return "Text"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    events_excute(event)


if __name__ == "__main__":
    app.run()
