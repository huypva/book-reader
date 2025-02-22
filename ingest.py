"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import ReadTheDocsLoader, UnstructuredMarkdownLoader, UnstructuredPDFLoader
# from langchain.document_loaders import ReadTheDocsLoader, UnstructuredMarkdownLoader,  PDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS


def ingest_docs():
    """Get documents from web pages."""
    # loader = ReadTheDocsLoader("./data/Get Your Hands Dirty on Clean Architecture (2019, Leanpub) - Tom Hombergs.pdf")
    loader = UnstructuredPDFLoader("./data/Clean Architecture A Craftsman Guide to Software Structure and Design.pdf")

    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    documents = text_splitter.split_documents(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
