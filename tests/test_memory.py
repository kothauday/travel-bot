from core.memory import get_memory, save_to_memory, clear_session
from langchain_core.messages import HumanMessage, AIMessage


def test_memory_starts_empty():
    clear_session("new-session")
    history = get_memory("new-session")
    assert history == []


def test_memory_saves_messages():
    clear_session("save-test")
    save_to_memory("save-test", "Hello", "Hi there!")
    history = get_memory("save-test")

    assert len(history) == 2
    assert isinstance(history[0], HumanMessage)
    assert isinstance(history[1], AIMessage)
    assert history[0].content == "Hello"
    assert history[1].content == "Hi there!"
    clear_session("save-test")


def test_memory_window_limit():
    clear_session("window-test")
    # Save 7 turns (14 messages) — window is 6 turns (12 messages)
    for i in range(7):
        save_to_memory("window-test", f"Q{i}", f"A{i}")

    history = get_memory("window-test")
    assert len(history) == 12  # only last 6 turns kept
    clear_session("window-test")


def test_clear_session():
    save_to_memory("clear-test", "Hello", "Hi!")
    clear_session("clear-test")
    history = get_memory("clear-test")
    assert history == []
