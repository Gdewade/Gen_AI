from langchain_community.document_loaders import UnstructuredExcelLoader

file_path="/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/sample_excel_file.xlsx"
 

loader=UnstructuredExcelLoader(file_path)
document=loader.load()

print(len(document))
print(document[0].page_content)
print(document[0].metadata)