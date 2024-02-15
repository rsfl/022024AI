#Modified by Rod Soto
import os 
os.environ['OPENAI_API_KEY'] =''
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate


cot_instruction = "Let's think step by step!"
cot_instruction2 = "Explain your reasoning step-by-step. Finally, state the answer."
reasoning_prompt = "{question}\n" + cot_instruction
prompt = PromptTemplate(
  template=reasoning_prompt,
  input_variables=["question"]
)

model = ChatOpenAI()
chain = prompt | model
print(chain.invoke({
   "question": "I had two Flipper Zeros. I lost 1. Then my friend gave me 2. How many Flipper Zeros do I have now?",
}))


if __name__ == "__main__":
    pass
