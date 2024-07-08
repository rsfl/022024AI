#use tavily internet search + ollama + llama3 via langchain
#written by Rod Soto, there is a problem with the max number of tokens the local model can take and longer prompts will  produce errors
#this needs a lot of fixing but it will get you started

import os
from langchain.llms import LlamaCpp
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults

# set up API key
os.environ["TAVILY_API_KEY"] = ""


llm = LlamaCpp(
    model_path="/path/to/model.gguf",
    temperature=0.7,
    max_tokens=2000,
    top_p=1,
    n_ctx=2048,
    verbose=True,
)
search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)

# initialize the agent
agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# run the agent
agent_chain.run(
    "What is Hackmiami?",
),
verbose = True

