from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-4o-mini")

length=input("Enter a length of report (short/medium/long) :")
topic=input("Enter a topic of report you want :")

prompt="Provide {} report on {}".format(length,topic)

print(prompt)

result=llm.invoke(prompt)
print(result.content)
