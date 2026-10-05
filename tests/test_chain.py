from unittest.mock import MagicMock, patch
from core.chain import build_rag_chain


def test_chain_returns_string():
    mock_retriever = MagicMock()
    mock_retriever.invoke.return_value = [
        MagicMock(page_content="Paris has the Eiffel Tower.")
    ]

    with patch("core.chain.ChatGoogleGenerativeAI") as MockLLM:
        mock_llm = MagicMock()
        mock_llm.return_value = "Paris is a great destination!"
        MockLLM.return_value = mock_llm

        run = build_rag_chain(mock_retriever, session_id="test-session")
        answer = run("Tell me about Paris")

    assert isinstance(answer, str)
    assert len(answer) > 0


def test_chain_saves_to_memory():
    from core.memory import get_memory, clear_session

    mock_retriever = MagicMock()
    mock_retriever.invoke.return_value = [
        MagicMock(page_content="Bali is in Indonesia.")
    ]

    with patch("core.chain.ChatGoogleGenerativeAI") as MockLLM:
        mock_llm = MagicMock()
        mock_llm.return_value = "Bali is beautiful!"
        MockLLM.return_value = mock_llm

        run = build_rag_chain(mock_retriever, session_id="mem-test")
        run("Tell me about Bali")

    history = get_memory("mem-test")
    assert len(history) == 2
    clear_session("mem-test")
