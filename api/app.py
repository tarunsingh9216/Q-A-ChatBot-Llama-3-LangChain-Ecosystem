from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A Simple API Server"
)

## LLM Model

llm = Ollama(model="Llama3.1")

prompt=ChatPromptTemplate.from_template("Write ma an essay about {topic} with 20 words")

add_routes(
    app,
    prompt|llm,
    path="/essay"
    
)

if __name__ == "__main":
    uvicorn.run(app, host="localhost", port=8000)


