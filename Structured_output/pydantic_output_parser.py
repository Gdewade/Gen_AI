from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from typing import Literal,Annotated,Optional
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from dotenv import load_dotenv
load_dotenv()


class ReviewAnalysis(BaseModel):
    summary:str=Field(min_length=20,max_len=50,description="short summary")
    sentiment:Literal["positive","negative","neutral"]=Field(description="sentiment of the review")
    pros:Annotated[Optional[list[str]],"list of all pros mentioned"]
    cons:Annotated[Optional[list[str]],"list of all cons mentioned"]

pydantic_parser_obj=PydanticOutputParser(pydantic_object=ReviewAnalysis)

prompt="this is the review:{review} \n {format_instruction}"
prompt_obj=PromptTemplate.from_template(prompt)
prompt_obj=prompt_obj.partial(format_instruction={"format_instrucion":pydantic_parser_obj.get_format_instructions()})
feedback_input="""
The Amazon app is generally useful for browsing and purchasing products online. It offers a wide selection of items, convenient payment options, and order tracking features. However, the app can sometimes be slow to load, and finding specific products may require scrolling through many sponsored results. While it gets the job done for most shopping needs, there is room for improvement in terms of performance and user experience. Overall, it's an average shopping app that works as expected most of the time.
"""
prompt_result=prompt_obj.invoke({"review":feedback_input})

llm_obj=ChatOpenAI(model="gpt-4o-mini")

llm_result=llm_obj.invoke(prompt_result)

pydantic_parser_result=pydantic_parser_obj.invoke(llm_result)

print(pydantic_parser_result)