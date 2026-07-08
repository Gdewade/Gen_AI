from langchain_community.document_loaders import CSVLoader

file=CSVLoader(file_path="/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/Student_Placement_Skills_2025.csv"
)

document=file.load()

print(len(document))

print(document[0].page_content)
print(document[0].metadata)



