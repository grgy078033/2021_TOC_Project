import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from flask.logging import create_logger
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine(
    states=["start",
            "lobby",
            "sharing",
            "boy", "girl",
            "boy_fast", "boy_slow", "girl_fast", "girl_slow",
            "boy_fast_crazy", "boy_fast_happy", "boy_slow_ease", "boy_slow_comfort", "girl_fast_crazy", "girl_fast_happy", "girl_slow_ease", "girl_slow_comfort"],
    transitions=[
        {
            "trigger": "advance",
            "source": "start",
            "dest": "lobby",
            "conditions": "is_going_to_lobby",
        },
        {
            "trigger": "advance",
            "source": "lobby",
            "dest": "sharing",
            "conditions": "is_going_to_sharing",
        },
        {
            "trigger": "advance",
            "source": "sharing",
            "dest": "boy",
            "conditions": "is_going_to_boy",
        },
        {
            "trigger": "advance",
            "source": "sharing",
            "dest": "girl",
            "conditions": "is_going_to_girl",
        },
        {
            "trigger": "advance",
            "source": "boy",
            "dest": "boy_fast",
            "conditions": "boy_to_fast",
        },
        {
            "trigger": "advance",
            "source": "boy",
            "dest": "boy_slow",
            "conditions": "boy_to_slow",
        },
        {
            "trigger": "advance",
            "source": "girl",
            "dest": "girl_fast",
            "conditions": "girl_to_fast",
        },
        {
            "trigger": "advance",
            "source": "girl",
            "dest": "girl_slow",
            "conditions": "girl_to_slow",
        },
        {
            "trigger": "advance",
            "source": "boy_fast",
            "dest": "boy_fast_crazy",
            "conditions": "boy_fast_to_crazy",
        },
        {
            "trigger": "advance",
            "source": "boy_fast",
            "dest": "boy_fast_happy",
            "conditions": "boy_fast_to_happy",
        },
        {
            "trigger": "advance",
            "source": "boy_slow",
            "dest": "boy_slow_ease",
            "conditions": "boy_slow_to_ease",
        },
        {
            "trigger": "advance",
            "source": "boy_slow",
            "dest": "boy_slow_comfort",
            "conditions": "boy_slow_to_comfort",
        },
        {
            "trigger": "advance",
            "source": "girl_fast",
            "dest": "girl_fast_crazy",
            "conditions": "girl_fast_to_crazy",
        },
        {
            "trigger": "advance",
            "source": "girl_fast",
            "dest": "girl_fast_happy",
            "conditions": "girl_fast_to_happy",
        },
        {
            "trigger": "advance",
            "source": "girl_slow",
            "dest": "girl_slow_ease",
            "conditions": "girl_slow_to_ease",
        },
        {
            "trigger": "advance",
            "source": "girl_slow",
            "dest": "girl_slow_comfort",
            "conditions": "girl_slow_to_comfort",
        },
        #------------------------------------------back----------------------------------------
        {"trigger": "advance", "source": ["boy", "girl"], "dest": "sharing", "conditions": "is_backing_to_gender"},
        {
            "trigger": "advance", 
            "source": ["boy_fast", "boy_slow"], 
            "dest": "boy", 
            "conditions": "is_backing_to_speed"
        },
        {
            "trigger": "advance", 
            "source": ["girl_fast", "girl_slow"], 
            "dest": "girl", 
            "conditions": "is_backing_to_speed"
        },
        {
            "trigger": "advance", 
            "source": ["boy_fast_crazy", "boy_fast_happy"], 
            "dest": "boy_fast", 
            "conditions": "is_backing_to_fast_type"
        },
        {
            "trigger": "advance", 
            "source": ["boy_slow_ease", "boy_slow_comfort"], 
            "dest": "boy_slow", 
            "conditions": "is_backing_to_slow_type"
        },
        {
            "trigger": "advance", 
            "source": ["girl_fast_crazy", "girl_fast_happy"], 
            "dest": "girl_fast", 
            "conditions": "is_backing_to_fast_type"
        },
        {
            "trigger": "advance", 
            "source": ["girl_slow_ease", "girl_slow_comfort"], 
            "dest": "girl_slow", 
            "conditions": "is_backing_to_slow_type"
        },
        {
            "trigger": "advance", 
            "source": ["boy_fast_crazy", "boy_fast_happy", "boy_slow_ease", "boy_slow_comfort", "girl_fast_crazy", "girl_fast_happy", "girl_slow_ease", "girl_slow_comfort"], 
            "dest": "sharing", 
            "conditions": "is_backing_to_choose_gender"
        },
        {
            "trigger": "advance", 
            "source": ["boy_fast_crazy", "boy_fast_happy", "boy_slow_ease", "boy_slow_comfort", "girl_fast_crazy", "girl_fast_happy", "girl_slow_ease", "girl_slow_comfort"], 
            "dest": "lobby", 
            "conditions": "is_backing_to_back_lobby"
        },
        {
            "trigger": "advance", 
            "source": "sharing", 
            "dest": "lobby", 
            "conditions": "is_share_backing_to_lobby"
        },
    ],
    initial="start",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")
LOG = create_logger(app)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    LOG.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    LOG.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response is False:
            send_text_message(event.reply_token, "請輸入正確訊息")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
