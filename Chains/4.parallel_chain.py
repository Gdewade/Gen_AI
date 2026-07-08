from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.scheme.runnable import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm_obj=ChatOpenAI(model="gpt-4o-mini")
prompt_obj_1=PromptTemplate(template="Generate short and simple notes from the following text \n {text}",
                            input_variables=["text"])
prompt_obj_2=PromptTemplate(template="Generate 5 short question answer from following text \n {text}",
                            input_variables=["text"])
prompt_obj_3=PromptTemplate(template="Merge the provided notes and quiz into single document \n notes -> {notes} and quiz -> {quiz}",
                            input_variables=["notes","quiz"])

parser_obj=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        "notes":prompt_obj_1 | llm_obj | parser_obj,
        "quiz" :prompt_obj_2 | llm_obj | parser_obj
    }
)

chain = parallel_chain | prompt_obj_3 | llm_obj | parser_obj

text="""
Generative Artificial Intelligence (GenAI) is a disruptive branch of AI designed to create original, human-like content—including text, images, computer code, music, and videos—based on patterns learned from massive datasets. According to global industry benchmarks like the Thomson Reuters Professional Services Report, 95% of professionals expect GenAI to become core to their workflow within the next five years. It has evolved from a pure engineering experiment into a major driver of global economic productivity.1. Market Size and Economic ImpactGDP Contribution: GenAI has the projected potential to add $7 trillion to the global GDP over the next decade.Corporate Value: The technology is expected to unlock trillions of dollars across key operational sectors, including marketing, customer service, and R&D.Investment Boom: A massive 78% of enterprise leaders plan to expand their GenAI budgets in the coming year, shifting from experimental proof-of-concepts to permanent production engines.2. Core Functional ApplicationsAutomated Reporting: Platforms leverage Large Language Models (LLMs) to automatically ingest unstructured enterprise metrics and parse them into polished business reports. Organizations using GenAI for automated reporting observe a 30% drop in generation time alongside a 25% jump in accuracy.Software Development: AI engines generate system code, deployment scripts, and tests. While it frees up time for creative engineering, data shows it can expand batch sizes, meaning proper code vetting remains critical.Multimodal Creation: Visual and auditory generators utilize advanced Transformer models to convert simple conversational text prompts into production-grade image, audio, or video components.3. Structural Shifts in EmploymentThe "GenAI Scientist" Era: Global data science job numbers are scaling rapidly, driven by specialized needs for AI, machine learning, and prompt engineers.Targeted Displacement: Employment shifts remain highly sector-specific. Most automation affects repetitive, back-office administration, data ingestion, and basic tele-calling, redirecting enterprise capital toward strategic human roles.4. Key Implementation BottlenecksThe Scale Frontier: Most enterprises struggle to advance more than 30% of their initial GenAI pilots into full organizational rollouts within a six-month window.Accuracy and Hallucinations: GenAI outputs can occasionally sound confident yet remain factually flawed, requiring continuous oversight, strict feedback loops, and human-in-the-loop verification.Data Security and Bias: Processing large operational datasets creates regulatory compliance risks (under frameworks like GDPR and CCPA) and calls for stringent data masking, encryption, and bias mitigation protocols.
"""

result=chain.invoke({"text":text})
print(result)
chain.get_graph().print_ascii()