# ollama_bot.py
import ollama

def ask_ollama(session_history, prompt):
    messages = [{"role": m["role"], "content": m["content"]} for m in session_history]
    messages.append({"role": "user", "content": prompt})
    response = ollama.chat(model="phi3:mini", messages=messages)
    return response["message"]["content"].strip()