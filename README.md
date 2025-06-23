Chatbot with Gemini & Ollama
----------------------------

Overview
--------
This is a command-line chatbot application built in Python that integrates:
- Gemini 1.5 (cloud-based, via Google Generative AI API)
- Ollama (local LLM like phi3:mini or similar)

It supports:
- Full conversational memory
- Seamless switching between Gemini and Ollama
- Auto-fallback to Ollama when Gemini quota is exhausted
- Commands like /reset and /exit

Features
--------
✅ Supports Gemini (gemini-1.5-flash) and Ollama engines  
✅ Maintains conversation history (context-aware responses)  
✅ Gracefully handles Gemini quota errors (HTTP 429)  
✅ Simple command-based UX (/reset, /exit)  
✅ Modular structure with separate files per component

Folder Structure
----------------
.
├── main.py             # Entry point – manages I/O and engine selection  
├── chat_session.py     # Handles chat history and session reset  
├── gemini_bot.py       # Contains Gemini API integration logic  
├── ollama_bot.py       # Contains Ollama local model logic  
├── .env                # Holds Gemini API key (not committed)  
├── requirements.txt    # Python dependencies  
└── README.txt          # Project overview and instructions

Requirements
------------
- Python 3.8+
- google-generativeai
- python-dotenv
- Ollama installed and running locally

Install dependencies:
---------------------
pip install -r requirements.txt

Create a .env file with your Gemini API key:
---------------------
GEMINI_API_KEY=your_actual_api_key

Run the chatbot:
---------------------
python main.py
