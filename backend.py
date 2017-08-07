from flask import Flask, request, abort
from linebot_commands import *

app = Flask(__name__)


@app.route("/", methods=['POST', "GET"])
def index():
    channel_access_token = os.environ.get("channel_access_token", "YOUR_CHANNEL_ACCESS_TOKEN")
    channel_secret = os.environ.get("channel_secre", "YOUR_CHANNEL_SECRET")
    print("toke=",channel_access_token)
    print("channel_secret=", channel_secret)
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
