from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import CSVLoader
import os

class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db"):
        self.persist_directory = persist_directory
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
        self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        
    def document_loader(self, file_path: str):
        loader = CSVLoader(file_path=file_path, encoding="utf-8",metadata_columns = [])
        documents = loader.load()
        return documents
    
    def create_vector_store(self, documents):
        text = self.text_splitter.split_documents(documents)
        vector_store = Chroma.from_documents(documents=text, embedding=self.embedding, persist_directory=self.persist_directory)
        vector_store.persist()
        return vector_store
    
    def load_vector_store(self):
        if os.path.exists(self.persist_directory) and os.listdir(self.persist_directory):
            vector_store = Chroma(persist_directory=self.persist_directory, embedding_function=self.embedding)
            return vector_store
        else:
            raise ValueError("Vector store does not exist. Please create it first.")
    