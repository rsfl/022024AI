import os
os.environ['OPENAI_API_KEY'] = ''
#os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain import HuggingFaceHub

llm =  OpenAI(temperature=0.9)

text = "What is Hackmiami?"
print(llm(text))
