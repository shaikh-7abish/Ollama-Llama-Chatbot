from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please response to the queries'),
        ('user', f'Question:{question}')
    ]
)

# streamlit framework
st.title('Langchain Demo with Llama')
input_text = st.text_input('Enter your Query')

# Ollama llama 2
llm = Ollama(model='llama3.2:1b')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
  st.write(chain.invoke({'question': input_text}))