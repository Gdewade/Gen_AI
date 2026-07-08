from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm_obj=ChatOpenAI(model="gpt-4o-mini")
prompt_obj1=PromptTemplate(template="Give me five facts of {topic}",
                           input_variables=["topic"])
prompt_obj2=PromptTemplate(template="Summary from the following text \n {text}",
                           input_variables=["text"])
parser_obj=StrOutputParser()

chain = prompt_obj1 | llm_obj | parser_obj | prompt_obj2 | llm_obj | parser_obj
result=chain.invoke({"topic" : "Climate change"})

print(result)

chain.get_graph().print_ascii()