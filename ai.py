import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AI_PROMPT = os.getenv(
    "AI_PROMPT",
    "You are a helpful Telegram AI assistant. Reply short and polite."
)

def get_ai_reply(user_message):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",   # fast + cheap
            input=f"{AI_PROMPT}\nUser: {user_message}"
        )

        return response.output_text

    except Exception as e:
        print("OPENAI ERROR:", e)
        return "AI response error — check Render logs."
