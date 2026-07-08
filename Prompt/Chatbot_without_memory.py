from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

bot=ChatOpenAI(model="gpt-4o-mini")

while True:
    user_msg=input("You :")
    if user_msg.lower()=="exit":
        break
    reply=bot.invoke(user_msg)
    print("AI :",reply.content)



