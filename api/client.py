import requests
import streamlit as st

def get_ollama_response(input_text):
    respponse = requests.post(
        "https://localhost:8000/essay/invoke",
        json={'input':{'topic':input_text}}
    )
    
## Streamlit Framework

st.title("LangChain Demo with Llama 3 API")
input_text=st.text_input("Write an essay on")

if input_text:
    st.write(get_ollama_response(input_text))
    
    
    
