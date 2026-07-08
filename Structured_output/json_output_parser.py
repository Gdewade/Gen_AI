from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()


llm_obj=ChatOpenAI(model="gpt-4o-mini")

json_obj=JsonOutputParser()

prompt="provide short report on {topic} \n {format_instruction}"
prompt_obj = PromptTemplate.from_template(prompt)
prompt_obj = prompt_obj.partial(format_instruction=json_obj.get_format_instructions())
final_prompt=prompt_obj.invoke({"topic":"climate change"})

query=final_prompt.text
llm_result=llm_obj.invoke(query)
json_result=json_obj.invoke(llm_result)
print(json_result)

