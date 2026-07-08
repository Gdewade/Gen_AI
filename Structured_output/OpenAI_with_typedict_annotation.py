from typing import TypedDict,Annotated
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-4o-mini")
class ReviewAnalysis(TypedDict):
    personal_info:Annotated[str,"Provide personal information in 2 line not more than that"]
    awards:Annotated[str,"Awards they achieved"]

structured_output = llm.with_structured_output(ReviewAnalysis)

input=" Who is best cricketer of india "

result = structured_output.invoke(input)
print(result)