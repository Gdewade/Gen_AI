from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.title("Information Generator")

prompt="Explain the {topic} of {subject} to child who is 12 year old in {lines} lines"

prompt_temp_obj=PromptTemplate(template=prompt)

topic=st.text_input("Provide a topic you want to know (Ex; functions)")
subject=st.text_input("Provide a subject of that topic (Ex; Python)")
lines=st.text_input("Provide how short explanation you want in lines (Ex; 4 )")

cmplt_prompt=prompt_temp_obj.invoke({"topic":topic,"subject":subject,"lines":lines})

final_prompt=cmplt_prompt.text

llm=ChatOpenAI(model="gpt-4o-mini")

if st.button("Generate"):
    if final_prompt:
        result=llm.invoke(final_prompt)
        st.write(result.content)
    else:
        st.warning("please submit your question first")




