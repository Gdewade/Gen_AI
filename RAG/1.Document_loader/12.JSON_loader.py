from langchain_community.document_loaders import JSONLoader

loader=JSONLoader(
    file_path="/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/sample.json",
    jq_schema=".",
    text_content=False
)

document=loader.load()

print(len(document))
print(document[0].page_content)
print(document[0].metadata)