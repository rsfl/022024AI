#example of simple prompt with langchain Rod Soto
import os

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = ''

from langchain_community.llms import OpenAI

# Initialize the language model
llm = OpenAI(temperature=0.9)

text = "What is Hackmiami?"

# Generate the response using the language model
try:
    response = llm.generate([text])  # Wrap the text in a list
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
