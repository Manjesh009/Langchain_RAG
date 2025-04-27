from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.outPut_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. you have to respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

##streamlit framework

st.title("Langchain Demo With LLAMA2")
input_text=st.text_input("Search the topic you want")

#ollama LLAma2 LLM

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
