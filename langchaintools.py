
import os
os.environ['OPENAI_API_KEY'] = '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'
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()

search = DuckDuckGoSearchResults()
search.run("obama")

