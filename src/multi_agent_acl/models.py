from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# ai_model = init_chat_model("google_genai:gemini-3.8-flash")
ai_model = init_chat_model("groq:openai/gpt-oss-120b")
