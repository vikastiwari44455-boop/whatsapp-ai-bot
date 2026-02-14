import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

AI_PROMPT = os.getenv(
    "AI_PROMPT",
    "You are a helpful Telegram AI assistant. Reply short and polite."
)

def get_ai_reply(user_message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"{AI_PROMPT}\nUser: {user_message}"
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # 🔥 VERY IMPORTANT DEBUG LINE
        print("GEMINI RESPONSE:", result)

        # If Gemini gives error
        if "candidates" not in result:
            return "Gemini error — check Render logs."

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("AI ERROR:", e)
        return "AI busy right now, try again."


