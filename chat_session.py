# chat_session.py
class ChatSession:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return self.history

    def reset(self):
        self.history = []
        
    def __str__(self):
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.history])