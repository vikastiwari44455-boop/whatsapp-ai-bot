import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

AI_PROMPT = os.getenv(
    "AI_PROMPT",
    "You are a helpful Telegram AI assistant. Reply short and polite."
)

def get_ai_reply(user_message):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"{AI_PROMPT}\nUser: {user_message}"}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=20)
        result = response.json()

        print("GEMINI RESPONSE:", result)  # debug in Render logs

        # ✅ Safe parsing
        if "candidates" in result and len(result["candidates"]) > 0:
            return result["candidates"][0]["content"]["parts"][0]["text"]

        if "error" in result:
            print("Gemini ERROR:", result["error"])
            return "AI busy right now, try again."

        return "No AI response received."

    except Exception as e:
        print("REQUEST ERROR:", e)
        return "Server AI error."
