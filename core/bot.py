from core.retriever import get_retriever
from core.chain import build_rag_chain
from core.memory import clear_session


class TravelBot:
    def __init__(self, session_id: str = "default"):
        self.session_id = session_id
        retriever = get_retriever()
        self._run = build_rag_chain(retriever, session_id)

    def chat(self, question: str) -> str:
        return self._run(question)

    def reset(self) -> None:
        clear_session(self.session_id)
        retriever = get_retriever()
        self._run = build_rag_chain(retriever, self.session_id)
