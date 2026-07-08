from langchain_community.document_loaders import TextLoader

file=TextLoader("doc.txt",encoding="utf-8")
document=file.load()
print(len(document))
print(type(document[0]))
print(document[0].page_content,"\n")
print(document[0].metadata) 