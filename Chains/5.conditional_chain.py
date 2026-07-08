from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

from dotenv import load_dotenv
load_dotenv()

class Feedback(BaseModel):
    sentiment:Literal["positive","negative"]=Field(description="give the sentiment of the feedback")

llm_obj=ChatOpenAI(model="gpt-4o-mini")
parser_obj=StrOutputParser()

parser_obj2=PydanticOutputParser(pydantic_object=Feedback)

prompt_obj_1=PromptTemplate(
    template="classify the sentiment of following text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser_obj2.get_fromat_instructions()}
)

classifier_chain = prompt_obj_1 | llm_obj | parser_obj2

prompt_obj_2=PromptTemplate(
    template="write an appropriate response to this positive feedback \n {feedback} ",
    input_variables=["feedback"]
)

prompt_obj_3=PromptTemplate(
    template="write an appropriate response to this negative feedback, feedback should be 2-3 liner only and specific \n {feedback} ",
    input_variables=["feedback"]
)

branch_chain=RunnableBranch((lambda x:x.sentiment == "positive",prompt_obj_2 | llm_obj | parser_obj),
                           (lambda x:x.sentiment == "negative",prompt_obj_3 | llm_obj | parser_obj),
                           RunnableLambda(lambda x:"Could not fine sentiment"))

chain = classifier_chain | branch_chain

feedback_input="""
The Amazon app is generally useful for browsing and purchasing products online. It offers a wide selection of items, convenient payment options, and order tracking features. However, the app can sometimes be slow to load, and finding specific products may require scrolling through many sponsored results. While it gets the job done for most shopping needs, there is room for improvement in terms of performance and user experience. Overall, it's an average shopping app that works as expected most of the time.
"""

result=chain.invoke({"feedback":feedback_input})
print(result)

chain.get_graph().print_ascii()