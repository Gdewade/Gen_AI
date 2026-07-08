from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

from dotenv import load_dotenv
load_dotenv()

llm_obj=ChatOpenAI(model="gpt-4o-mini")

prompt_obj=PromptTemplate(template="Provide answer for following query /n {query} from following {text}",
                          input_variables=["query","text"])

parser_obj=StrOutputParser()

file=WebBaseLoader(web_path="https://en.wikipedia.org/wiki/2026_Iran_war")
document=file.load()

doc=document[0].page_content

final_context=doc[5000:10000]

print("-----> this is extracted text from web",final_context)

chain = prompt_obj | llm_obj | parser_obj

result=chain.invoke({"query":"Provide me information about iran-us war of 2026",
                     "text":final_context})

print("--------> this is the result from llm",result)