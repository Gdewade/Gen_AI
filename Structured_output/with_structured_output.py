from langchain_openai import ChatOpenAI
from typing import TypedDict

from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-4o-mini")

class ReportReview(TypedDict):
    Name:str
    Overview:str
    Age:int

structured_model = llm.with_structured_output(ReportReview)

input = "Who is best cricketer of india"
result=structured_model.invoke(input)
print(result)