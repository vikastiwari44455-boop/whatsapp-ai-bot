import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

# read variables
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AI_PROMPT = os.getenv("AI_PROMPT")
