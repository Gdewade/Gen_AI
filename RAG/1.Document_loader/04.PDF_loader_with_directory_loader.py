from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

#folder 1
file=DirectoryLoader(
    path = "/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/folder1" , 
    glob="*.pdf" ,
    loader_cls=PyPDFLoader
)

document=file.load()
print(len(document))
print(document[134].page_content)