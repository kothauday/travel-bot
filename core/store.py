from langchain_core.documents import Document
from langchain_chroma import Chroma
from core.embeddings import get_embeddings
from config import CHROMA_PERSIST_DIR, COLLECTION_NAME


def get_vector_store() -> Chroma:
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_PERSIST_DIR,
    )


def build_vector_store(chunks: list[Document]) -> Chroma:
    store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PERSIST_DIR,
    )
    print(f"[store] indexed {len(chunks)} chunks")
    return store
