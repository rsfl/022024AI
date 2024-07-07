

from langchain_community.llms import Ollama
ollama = Ollama(
    base_url='http://localhost:11434',
    model="llama3"
)
print(ollama.invoke("What is Hackmiami?"))