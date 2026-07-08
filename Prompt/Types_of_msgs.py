from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

bot=ChatOpenAI(model="gpt-4o-mini")

dialogue=[
    SystemMessage(content="You are a helpful AI tutor"),
    HumanMessage(content="Tell me about langgraph content"),
    AIMessage(content="Langgraph is a framework for building Agentic AI Applications"),
    HumanMessage(content="What are its key features")
]

response=bot.invoke(dialogue)
dialogue.append(AIMessage(content=response.content))
print("---------------------------------------------")
print(dialogue)

