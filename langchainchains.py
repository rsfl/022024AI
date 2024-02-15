#modified by Rod Soto
import os
os.environ['OPENAI_API_KEY'] = ''
#os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
from langchain_community.llms import OpenAI
#from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from langchain.memory import ConversationBufferWindowMemory

llm =  OpenAI()

prompt = """Question: Can we time travel?

Let's think step by step.

Answer: """
llm(prompt)


template = """Question: {question}

Let's think step by step.

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])


llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Can we time travel?"

print(llm_chain.run(question))
