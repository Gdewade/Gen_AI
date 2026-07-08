from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
My name is Alice.I am 28 years old.

I live in Boston.How are you."""

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=18,
    chunk_overlap=3.6
)

docs=text_splitter.split_text(text)
print(len(docs))

print("Chunk ------->",docs[0])
print("Chunk ------->",docs[1])
print("Chunk ------->",docs[2])
print("Chunk ------->",docs[3])
print("Chunk ------->",docs[4])
print("Chunk ------->",docs[5])


