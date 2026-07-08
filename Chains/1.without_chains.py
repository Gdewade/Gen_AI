from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm_obj=ChatOpenAI(model="gpt-4o-mini")

prompt_obj=PromptTemplate(template="Give me five facts about {topic}",
                          input_variables=["topic"])

parser_obj=StrOutputParser()

prompt_result=prompt_obj.invoke({"topic":"Agentic AI"})
llm_result=llm_obj.invoke(prompt_result)
parser_result=parser_obj.invoke(llm_result)

print(parser_result)
