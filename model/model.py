from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")
