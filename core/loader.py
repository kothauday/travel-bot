from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    JSONLoader,
    TextLoader,
)


def load_documents(data_dir: str = "./data/raw") -> list[Document]:
    path = Path(data_dir)
    docs: list[Document] = []

    loaders = [
        ("**/*.pdf",  lambda p: PyPDFLoader(str(p))),
        ("**/*.csv",  lambda p: CSVLoader(str(p))),
        ("**/*.txt",  lambda p: TextLoader(str(p), encoding="utf-8")),
        ("**/*.json", lambda p: JSONLoader(str(p), jq_schema=".", text_content=False)),
    ]

    for pattern, make_loader in loaders:
        for file in path.glob(pattern):
            try:
                docs.extend(make_loader(file).load())
            except Exception as exc:
                print(f"[loader] skipping {file.name}: {exc}")

    print(f"[loader] loaded {len(docs)} documents")
    return docs
