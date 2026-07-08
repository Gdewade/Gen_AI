from langchain_openai import ChatOpenAI
from typing import TypedDict,Annotated,Optional,Literal

from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-4o-mini")
class ReviewAnalysis(TypedDict):
    summary:Annotated[str,"Provide summary in 1 line not more than that"]
    sentiment:Annotated[Literal["Positive","Negative","Neutral"],"only in positive , negative and neutral"]
    pros:Annotated[Optional[list[str]],"list of all pros mentioned"]
    cons:Annotated[Optional[list[str]],"list of all cons mentioned"]

structured_output = llm.with_structured_output(ReviewAnalysis)

input="""
The Amazon app is generally useful for browsing and purchasing products online. It offers a wide selection of items, convenient payment options, and order tracking features. However, the app can sometimes be slow to load, and finding specific products may require scrolling through many sponsored results. While it gets the job done for most shopping needs, there is room for improvement in terms of performance and user experience. Overall, it's an average shopping app that works as expected most of the time."""


result = structured_output.invoke(input)

print(result)
