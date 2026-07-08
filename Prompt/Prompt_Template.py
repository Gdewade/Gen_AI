from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

tmpl="Write a poem about {subject} in a {mood} tone with {lines} lines."

prompt_temp_obj=PromptTemplate(template=tmpl)

subject=input("Enter a subject or topic :")
mood=input("Enter a tone/mood :")
lines=int(input("Enter lines :"))

response = prompt_temp_obj.invoke ({"subject":subject,"mood":mood,"lines":lines})

final_prompt=response.text

print(final_prompt)

llm=ChatOpenAI(model="gpt-4o-mini")

result=llm.invoke(final_prompt)
print(result.content)