from flask import Flask, request
import requests
import os
from ai import get_ai_reply

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

print("APP.PY LOADED")   # ✅ Debug to confirm new code runs


@app.route("/webhook", methods=["POST"])
def telegram_webhook():

    data = request.json
    print("MESSAGE RECEIVED:", data)   # ✅ See full Telegram payload

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")

        print("USER TEXT:", user_text)   # ✅ Confirm message text

        if user_text:
            print("CALLING AI...")       # ✅ Check if AI function runs
            ai_reply = get_ai_reply(user_text)
            print("AI REPLY:", ai_reply) # ✅ See AI output
            send_message(chat_id, ai_reply)

    return "ok"


@app.route("/")
def home():
    return "Telegram AI Bot Running"


def send_message(chat_id, text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    requests.post(url, json=payload)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
