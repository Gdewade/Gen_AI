from langchain_community.document_loaders import WebBaseLoader

urls=["https://docs.langchain.com/oss/python/langchain/quickstart",
     "https://docs.langchain.com/oss/python/langchain/agents",
     "https://docs.langchain.com/oss/python/langchain/models"]

file=WebBaseLoader(web_path=urls)
document=file.load()

print(len(document))
print(document[2].metadata)
print(document[1].page_content)