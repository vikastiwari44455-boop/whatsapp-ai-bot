import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

AI_PROMPT = os.getenv(
    "AI_PROMPT",
    "You are a helpful Telegram AI assistant. Reply short and polite."
)

def get_ai_reply(user_message):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": AI_PROMPT + "\nUser: " + user_message}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Sorry, I couldn't generate a reply."
