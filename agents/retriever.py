from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_vectorstore():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory="chroma_index", embedding_function=embedding)

def retrieve_docs(query, k=3):
    vectorstore = get_vectorstore()
    return vectorstore.similarity_search(query, k=k)
