from flask import Flask, request
import requests, os

app = Flask(__name__)

WXWORK_KEY = os.environ.get("WXWORK_KEY", "580db0e5-0dbc-44a2-8378-e761edd05938")
WXWORK_URL = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={WXWORK_KEY}"

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.get_data(as_text=True)
    requests.post(WXWORK_URL, json={"msgtype": "text", "text": {"content": msg}})
    return "ok"

if __name__ == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
