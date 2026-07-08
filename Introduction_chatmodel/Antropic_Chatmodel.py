from dotenv import load_dotenv
load_dotenv()

from langchain_antropic import ChatAnthropic

llm=ChatAnthropic(model="")

response=llm.invoke("What is capital of china")
print(response.content)