import streamlit as st
import requests

def get_gemini_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
                           json={'input':{'topic':input_text}})
    
    return response.json()["output"]["content"]

def get_poem_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic':input_text}})
    
    return response.json()["output"]["content"]



st.title("LangChain Demo With Gemini And LLAMA2")
text2=st.text_input("Write a poem on??")
text1=st.text_input("Write an essay on??")

if text2:
    st.write(get_poem_response(text2))
if text1:
    st.write(get_gemini_response(text1))