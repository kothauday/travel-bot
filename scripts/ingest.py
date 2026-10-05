"""Run once to build the Chroma vector index from files in data/raw/."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.loader import load_documents
from core.chunker import chunk_documents
from core.store import build_vector_store


def main():
    docs = load_documents("./data/raw")
    if not docs:
        print("No documents found. Add files to data/raw/ and re-run.")
        return
    chunks = chunk_documents(docs)
    build_vector_store(chunks)
    print("Ingestion complete.")


if __name__ == "__main__":
    main()
