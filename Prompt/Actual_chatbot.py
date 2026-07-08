from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

bot=ChatOpenAI(model="gpt-4o-mini")
SYSTEM_ROLE = "You are a helpful AI Tutor, provide answer in one liner only"

dialogue=[SystemMessage(content=SYSTEM_ROLE)]

while True:
    user_input=input("You :")
    if user_input.lower()=="exit":
        break
    dialogue.append(HumanMessage(content=user_input))
    question=bot.invoke(dialogue) # question means the humanmsg 
    answer=question.content       # answer means the ai reply on human msg
    dialogue.append(AIMessage(content=answer))
    print(f"AI:{answer}\n")

