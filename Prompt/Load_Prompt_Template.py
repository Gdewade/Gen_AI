from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

loaded_prompt=load_prompt("poem_template.json")

subject=input("Enter a subject of your poem :")
lines=int(input("Enter how many lines poem you want :"))

cmplt_prompt=loaded_prompt.invoke({"subject":subject,"lines":lines})

final_prompt=cmplt_prompt.text

llm=ChatOpenAI(model="gpt-4o-mini")

final_response=llm.invoke(final_prompt)
print(final_response.content)