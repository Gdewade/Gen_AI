from langchain_community.document_loaders import UnstrcuturedLoader

file_path="/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/sample.html"
loader=UnstrcuturedLoader(file_path)
document=loader.load()
print(len(document))

for i,doc in enumerate(document):
    print("document",i+1)
    print("content",doc.page_content)
    print("metadata",doc.metadata)
