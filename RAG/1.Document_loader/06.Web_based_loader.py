from langchain_community.document_loaders import WebBaseLoader

url="https://docs.langchain.com/oss/python/langchain/quickstart"

file=WebBaseLoader(web_path=url)

document=file.load()

print(len(document))
print(document[0].page_content)
print(document[0].metadata)