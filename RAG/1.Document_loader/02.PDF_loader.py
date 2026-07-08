from langchain_community.document_loaders import PyPDFLoader

file=PyPDFLoader("Python_Training_Slides_With_Images.pdf")
document=file.load()

print(len(document)) # pages of pdf
print(document[43])
print(document[0].page_content,"\n")
print(document[0].metadata)