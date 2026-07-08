from langchain_community.document_loaders import UnstructuredMarkdownLoader

file_path="/mnt/c/Users/Gayatri/OneDrive/Desktop/Agentic_AI/Gen_AI/RAG/sample_markdown_file.md"
loader=UnstructuredMarkdownLoader(file_path)
document=loader.load()

print(len(document))
print(document[0].metadata)
print(document[0].page_content)
