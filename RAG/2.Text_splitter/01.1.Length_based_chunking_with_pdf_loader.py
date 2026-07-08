from langchain_coummunity.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

pdf_loader=PyPDFLoader("Python_Training_Slides_With_Images.pdf")
documents=pdf_loader.load()

text_splitters=CharacterTextSplitter(chunk_size=500,chunk_overlap=50,separator=" ")
chunks=text_splitters.split_documents(documents)

print(f"Pages :{len(documents)}, Chunks :{len(chunks)}")

