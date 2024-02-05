import os
os.environ['OPENAI_API_KEY'] = ''
#os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
#from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from langchain.memory import ConversationBufferWindowMemory

llm =  OpenAI()


prompt_template = PromptTemplate.from_template(
    template="Write a {length} story about: {content}"
)

llm = OpenAI()

prompt = prompt_template.format(
    length="2-sentence",
    content="The hometown of the legendary nuclear scientist, J. Robert Oppenheimer"
)

response = llm.predict(
    text=prompt
)

print(response)