from langchain_community.document_loaders import TextLoader,DirectoryLoader

#folder 2
file=DirectoryLoader(
    path="/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/folder2",
    glob="*.txt",
    loader_cls=TextLoader

)

document=file.load()

print(len(document))

print(document[0].metadata)

print(document[0].page_content)
print(document[1].page_content)
print(document[2].page_content)
