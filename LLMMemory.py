import os
os.environ['OPENAI_API_KEY'] = ''
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0.2)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

print(conversation.predict(input="Is Start Wars a good movie?"))

print(conversation.predict(input="Who is the main bad guy?"))

print(conversation.predict(input="I heard Han Solo died is that true?"))