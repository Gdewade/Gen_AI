from langchain_core.prompts import PromptTemplate

tmpl="Write a poem about {subject} with {lines} lines"

prompt_obj=PromptTemplate(template=tmpl)

prompt_obj.save("poem_template.json")