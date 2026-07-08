from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-5.4-mini",)

response=llm.invoke("Provide me python code for prime number")
print(response.content)