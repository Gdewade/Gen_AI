from langchain_community.document_loaders import BSHTMLLoader

loader=BSHTMLLoader("sample.html")

document=loader.load()

print(len(document))
print(document[0].page_content)
print(document[0].metadata)