from dotenv import load_dotenv
import os

load_dotenv()

# Google Gemini — used for LLM chat responses
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# LLM
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.5-flash-lite")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.4"))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "512"))

# Embeddings — local HuggingFace model (no API key needed)
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Vector store
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/processed/chroma_db")
COLLECTION_NAME = "travel_knowledge"
RETRIEVER_K = int(os.getenv("RETRIEVER_K", "4"))

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))

# Memory
MEMORY_WINDOW_K = int(os.getenv("MEMORY_WINDOW_K", "6"))
