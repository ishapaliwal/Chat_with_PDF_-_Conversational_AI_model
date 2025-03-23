# fileingestor.py
import streamlit as st
from langchain.chains import ConversationalRetrievalChain
import tempfile
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from loadllm import Loadllm
from langchain_community.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings  # Updated import
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.embeddings import HuggingFaceEmbeddings
class FileIngestor:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def handlefileandingest(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(self.uploaded_file.getvalue())
            tmp_file_path = temp_file.name

        pdf_loader = PyMuPDFLoader(file_path=tmp_file_path)
        document_data = pdf_loader.load()

        # embeddings_model = HuggingFaceEmbeddings(
        #     model_name="sentence-transformers/all-MiniLM-L6-v2"
        # )
        #embeddings_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")  # Simplified embeddings
        from langchain_community.embeddings import HuggingFaceEmbeddings

        embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        vector_store = FAISS.from_documents(document_data, embeddings_model)
        vector_store.save_local("vectorstore/db_faiss")

        # Load LLM and prepare conversational chain
        if "llm" not in st.session_state:
            st.session_state["llm"] = Loadllm.load_llm()
        if "chain" not in st.session_state:
            st.session_state["chain"] = ConversationalRetrievalChain.from_llm(
                st.session_state["llm"], vector_store.as_retriever()
            )