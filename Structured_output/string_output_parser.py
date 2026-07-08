from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()


llm_obj=ChatOpenAI(model="gpt-4o-mini")
query="what is capital of iran"
llm_result = llm_obj.invoke(query)

parser_obj=StrOutputParser()
parser_result=parser_obj.invoke(llm_result)
print(parser_result)
