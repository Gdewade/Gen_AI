from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()


llm_obj=ChatOpenAI(model="gpt-4o-mini")
parser_obj=StrOutputParser()
prompt_obj=PromptTemplate(template="Provide the answer for following query /n {query}",
                          input_variables=["query"])

file=TextLoader("query.txt",encoding="utf-8")

document=file.load()

query=document[0].page_content

chain=prompt_obj | llm_obj | parser_obj

result=chain.invoke({"query":query})

print(result)
