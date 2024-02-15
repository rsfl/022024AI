import os
os.environ['OPENAI_API_KEY'] = ''

from langchain_community.llms import OpenAI  
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from langchain.memory import ConversationBufferWindowMemory

# Initialize the language model
llm = OpenAI()

prompt_template = PromptTemplate.from_template(
    template="Write a {length} story about: {content}"
)

prompt = prompt_template.format(
    length="2-sentence",
    content="The hometown of the legendary nuclear scientist, J. Robert Oppenheimer"
)

response = llm.predict(text=prompt)  

print(response)

