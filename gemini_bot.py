# gemini_bot.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(session_history, prompt):
    messages = [{"role": h["role"], "parts": [h["content"]]} for h in session_history]
    messages.append({"role": "user", "parts": [prompt]})
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(messages)
    return response.text.strip()