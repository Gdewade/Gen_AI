from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint



llm_obj=HuggingFaceEndpoint(repo_id="Qwen/Qwen3-32B")
# llm_obj=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct")

chat=ChatHuggingFace(llm=llm_obj)

response=chat.invoke("Captial of china")
print(response.content)