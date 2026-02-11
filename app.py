from flask import Flask, request
import requests
from config import ACCESS_TOKEN, PHONE_NUMBER_ID, VERIFY_TOKEN
from ai import ask_ai

app = Flask(__name__)

def send_message(to, text):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }

    requests.post(url, headers=headers, json=data)


@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge
    return "Error"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = msg["from"]
        text = msg["text"]["body"]

        reply = ask_ai(text)

        send_message(sender, reply)

    except Exception as e:
        print("Error:", e)

    return "OK", 200


if __name__ == "__main__":
    app.run(port=5000)
