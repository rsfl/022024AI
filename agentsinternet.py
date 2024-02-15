# libraries
import os

from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain import FewShotPromptTemplate


# set up API key
os.environ["TAVILY_API_KEY"] = 
os.environ['OPENAI_API_KEY'] = 

# set up the agent
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)
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
    "What is the JellyFish UAP?",
)