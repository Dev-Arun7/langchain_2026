import langchain
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API")
os.environ["GROQ_API_KEY"]= os.getenv("GORQ_API")



from langchain.chat_models import init_chat_model

my_model = init_chat_model(
    model="gemini-3.1-flash-lite",
    model_provider="google_genai"
)



response2 = my_model.invoke("What you think about future of developer job since ai growing like carazy?")
print(response2)



from langchain.chat_models import init_chat_model

my_model = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="groq"
)

