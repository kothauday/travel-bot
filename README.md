# ✈️ Travel Chatbot — RAG with LangChain + Gemini

A Retrieval-Augmented Generation (RAG) travel assistant built with LangChain, ChromaDB, Google Gemini, and Streamlit. Ask questions about destinations, hotels, flights, and travel packages — all answers are grounded in your own knowledge base files.

---

## What is RAG?

RAG stands for **Retrieval-Augmented Generation**. Instead of relying purely on the AI model's training data, RAG:

1. **Retrieves** relevant information from your own documents (PDFs, CSVs, etc.)
2. **Augments** the prompt with that retrieved context
3. **Generates** an answer grounded in your actual data

This means the bot answers based on YOUR travel data files — not generic internet knowledge.

---

## How It Works (Step by Step)

```
You type a question
        │
        ▼
Question is converted to a vector (list of numbers)
using HuggingFace all-MiniLM-L6-v2 (runs locally, free)
        │
        ▼
ChromaDB searches your indexed documents
and finds the 4 most relevant chunks
        │
        ▼
Those chunks + your chat history + your question
are combined into a prompt
        │
        ▼
Google Gemini reads the prompt and generates an answer
        │
        ▼
Answer is shown in the Streamlit chat UI
Chat history is saved for follow-up questions
```

---

## Project Structure

```
travel_bot/
│
├── app.py                     # Streamlit chat UI — the only file you run
├── config.py                  # All settings, reads values from .env
├── requirements.txt           # All Python packages
├── .env                       # Your secret API key (never share this)
├── .env.example               # Template showing what goes in .env
│
├── .streamlit/
│   └── config.toml            # Disables file watcher (prevents warning spam)
│
├── data/
│   ├── raw/                   # Your source documents — add files here
│   │   ├── destination_guide.pdf
│   │   ├── hotels.csv
│   │   ├── flight_routes.csv
│   │   └── package_deals.csv
│   └── processed/
│       └── chroma_db/         # Vector database — auto-created by ingest.py
│
├── core/                      # All RAG logic in one flat folder
│   ├── bot.py                 # TravelBot class — ties everything together
│   ├── chain.py               # RAG pipeline with Gemini LLM
│   ├── prompt.py              # System instructions sent to Gemini
│   ├── memory.py              # Stores last 6 messages per session
│   ├── retriever.py           # Finds top 4 relevant chunks per question
│   ├── embeddings.py          # Converts text to vectors (HuggingFace, local)
│   ├── store.py               # Saves and loads ChromaDB vector store
│   ├── loader.py              # Reads PDF, CSV, TXT, JSON from data/raw/
│   └── chunker.py             # Splits large docs into 800-char chunks
│
└── scripts/
    └── ingest.py              # Run once to index your documents into ChromaDB
```

---

## Tech Stack

| Component | Technology | Cost |
|---|---|---|
| LLM | Google Gemini `gemini-3.5-flash-lite` | Free (1500 req/day) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` | Free, runs locally |
| Vector Store | ChromaDB | Free, runs locally |
| RAG Framework | LangChain | Open source |
| UI | Streamlit | Open source |

---

## Prerequisites

- Python 3.10 or higher
- Google Gemini API key (free) — sign in at [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and click **Create API key**

---

## Setup (First Time Only)

### Step 1 — Create virtual environment

```powershell
cd travel_bot
python -m venv venv
.\venv\Scripts\activate
```

### Step 2 — Install dependencies

```powershell
pip install -r requirements.txt
pip install sentence-transformers langchain-huggingface langchain-google-genai
```

### Step 3 — Add your Gemini API key

Open the `.env` file and set your key:

```
GOOGLE_API_KEY=your_actual_gemini_key_here
LLM_MODEL=gemini-3.5-flash-lite
LLM_TEMPERATURE=0.4
LLM_MAX_TOKENS=512
CHROMA_PERSIST_DIR=./data/processed/chroma_db
RETRIEVER_K=4
CHUNK_SIZE=800
CHUNK_OVERLAP=100
MEMORY_WINDOW_K=6
```

### Step 4 — Build the vector store

Reads all files in `data/raw/`, splits them into chunks, converts to vectors, and saves to ChromaDB. Run once only.

```powershell
python scripts/ingest.py
```

Expected output:
```
[loader] loaded 56 documents
[chunker] 56 docs → 64 chunks
[store] indexed 64 chunks
Ingestion complete.
```

---

## Running the Project

Just one command:

```powershell
cd travel_bot
.\venv\Scripts\activate
streamlit run app.py
```

Browser opens automatically at `http://localhost:8501`.

On first launch you will see **"Loading travel knowledge base..."** for about 15 seconds while the embedding model loads. After that every message is instant.

---

## Using the Bot

- Type your question in the chat box and press Enter
- The bot retrieves relevant context from your data files and answers
- Ask follow-up questions — it remembers the last 6 messages
- Click **Clear Chat** in the sidebar to start a fresh conversation

### Example questions
- "What are the best hotels in Paris?"
- "Show me flights from New York to Tokyo"
- "What travel packages are available for Europe?"
- "What is the price range for hotels in Bali?"

---

## Adding New Data

1. Drop new files into `data/raw/` — supports PDF, CSV, TXT, JSON
2. Re-run ingestion:
   ```powershell
   .\venv\Scripts\activate
   python scripts/ingest.py
   ```
3. Restart Streamlit

---

## Troubleshooting

**"Loading travel knowledge base..." takes long**
Normal on first run — the HuggingFace model loads once and is cached. Subsequent launches are faster.

**Port 8501 already in use**
```powershell
Get-NetTCPConnection -LocalPort 8501 | Select-Object -ExpandProperty OwningProcess | ForEach-Object { Stop-Process -Id $_ -Force }
```

**Something went wrong error in chat**
Check that your `GOOGLE_API_KEY` in `.env` is correct and that you have internet access.

**Quota exceeded (429 error)**
You hit the free tier limit (1500/day). Wait until the next day — quota resets at midnight.

---

## Configuration Reference

All settings live in `config.py` and can be overridden via `.env`:

| Setting | Default | Description |
|---|---|---|
| `GOOGLE_API_KEY` | — | Your Gemini API key (required) |
| `LLM_MODEL` | `gemini-3.5-flash-lite` | Gemini model to use |
| `LLM_MAX_TOKENS` | `512` | Max tokens in each response |
| `RETRIEVER_K` | `4` | Number of chunks retrieved per question |
| `CHUNK_SIZE` | `800` | Characters per document chunk |
| `CHUNK_OVERLAP` | `100` | Overlap between chunks |
| `MEMORY_WINDOW_K` | `6` | Number of past messages remembered |
| `CHROMA_PERSIST_DIR` | `./data/processed/chroma_db` | Vector store location |
