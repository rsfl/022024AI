import os
#os.environ['OPENAI_API_KEY'] = ''
os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain import HuggingFaceHub

llm = llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature":1, "max_length":64})

text = "Where is the capital of Texas?"
print(llm(text))
