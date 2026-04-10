from flask import Flask, request
import requests, os

app = Flask(__name__)

WXWORK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=580db0e5-0dbc-44a2-8378-e761edd05938"

@app.route("/", methods=["GET", "POST"])
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    msg = request.get_data(as_text=True) or "测试信号"
    requests.post(WXWORK_URL, json={"msgtype": "text", "text": {"content": msg}})
    return "ok", 200
