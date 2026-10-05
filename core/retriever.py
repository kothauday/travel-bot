from langchain_core.vectorstores import VectorStoreRetriever
from core.store import get_vector_store
from config import RETRIEVER_K


def get_retriever() -> VectorStoreRetriever:
    store = get_vector_store()
    return store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": RETRIEVER_K,
            "fetch_k": RETRIEVER_K * 3,
            "lambda_mult": 0.6,
        },
    )
