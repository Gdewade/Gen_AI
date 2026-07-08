from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-4o-mini")
query="Who is best cricketer of india"

llm_obj=llm.invoke(query)

print(llm_obj.content)