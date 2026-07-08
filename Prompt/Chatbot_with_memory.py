from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

bot=ChatOpenAI(model="gpt-4o-mini")

memory=[]

while True:

    user_msg=input("You:")
    if user_msg.lower()=="exit":
        break
    memory.append(user_msg)
    reply=bot.invoke(user_msg)
    memory.append(reply.content)
    print("AI: ",reply.content)
    print("-----------------------")

print(memory)