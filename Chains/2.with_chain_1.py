from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt_obj=PromptTemplate(template="Give me five facts about {topic}",
                          input_variable=["topic"])

llm_obj=ChatOpenAI(model="gpt-4o-mini")
parser_obj=StrOutputParser()

chain= prompt_obj | llm_obj | parser_obj
result=chain.invoke({"topic":"Agentic AI"})
print(result)

chain.get_graph().print_ascii()