# main.py
"""
Console chatbot that can use Gemini (cloud) or Ollama (local).
Gracefully handles Gemini 429 quota errors and can /reset memory.
"""

from time import sleep
from chat_session import ChatSession
from gemini_bot import ask_gemini
from ollama_bot import ask_ollama
import google.api_core.exceptions as gex

def choose_engine() -> str:
    engine = input("Choose engine [gemini / ollama]: ").strip().lower()
    if engine not in ("gemini", "ollama"):
        print("Invalid choice. Exiting.")
        exit(1)
    return engine

def main() -> None:
    print("🤖 Welcome to the Console Chatbot")
    engine = choose_engine()
    session = ChatSession()

    print("Type your message.  /reset clears memory, /exit quits.")
    while True:
        prompt = input("You: ").strip()

        if prompt.lower() in ("/exit", "/quit"):
            break
        if prompt.lower() == "/reset":
            session.reset()
            print("🔄 Chat memory cleared.")
            continue

        session.add_message("user", prompt)

        try:
            reply = (
                ask_gemini(session.get_history(), prompt)
                if engine == "gemini"
                else ask_ollama(session.get_history(), prompt)
            )

        # Gemini quota exhausted → retry or switch engine
        except gex.ResourceExhausted as e:
            wait = getattr(e, "retry_delay", None)
            print("⚠️  Gemini quota exhausted.")
            if wait:
                print(f"   Retrying in {wait.seconds}s …")
                sleep(wait.seconds)
                continue           # retry same prompt
            # daily limit hit → fall back to Ollama
            print("   Switching to Ollama (local).")
            engine = "ollama"
            reply = ask_ollama(session.get_history(), prompt)

        print(f"{engine.title()}: {reply}")
        session.add_message("assistant", reply)

if __name__ == "__main__":
    main()