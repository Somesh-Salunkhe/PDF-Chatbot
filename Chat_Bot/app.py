# Q & A Chatbot

# Imports
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

# load environment variables from .env
load_dotenv()

# Load API key
API = os.getenv("API")

# Function to load model and get response

def get_model_response(query):
    
    # Initialize model
    model = ChatGroq(api_key=API, model= 'llama-3.1-8b-instant', temperature =0.5, max_tokens=1024)

    # Response
    response = model.invoke(query).content

    return response

# Initialize Streamlit app

## Page setup
st.set_page_config(page_title="Q & A Chatbot")
st.header("Langchain Application")


input = st.text_input("Your Question: ", key='input')
response = get_model_response(input)



## Submit Button
submit =st.button("Submit")

if submit:
    st.subheader("Answer: ")
    st.write(response)
