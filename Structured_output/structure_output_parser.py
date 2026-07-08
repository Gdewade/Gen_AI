from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from dotenv import load_dotenv
load_dotenv()


llm_obj = ChatOpenAI(model="gpt-4o-mini")

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic")
]

str_parser_obj = StructuredOutputParser.from_response_schemas(schema)

tmpl = """
Write three facts about {topic}

{format_instruction}
"""

prompt_obj = PromptTemplate.from_template(tmpl)

prompt_obj = prompt_obj.partial(
    format_instruction=str_parser_obj.get_format_instructions()
)

prompt_result = prompt_obj.invoke(
    {"topic": "impact of climate change on humans"}
)

llm_result = llm_obj.invoke(prompt_result)

str_parser_result = str_parser_obj.invoke(llm_result)

print(str_parser_result)