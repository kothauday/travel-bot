from langchain_core.messages import HumanMessage, AIMessage
from config import MEMORY_WINDOW_K

_sessions: dict[str, list] = {}


def get_memory(session_id: str) -> list:
    if session_id not in _sessions:
        _sessions[session_id] = []
    return _sessions[session_id]


def save_to_memory(session_id: str, question: str, answer: str) -> None:
    history = get_memory(session_id)
    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=answer))
    if len(history) > MEMORY_WINDOW_K * 2:
        _sessions[session_id] = history[-(MEMORY_WINDOW_K * 2):]


def clear_session(session_id: str) -> None:
    _sessions.pop(session_id, None)
