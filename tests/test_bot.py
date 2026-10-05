from unittest.mock import MagicMock, patch


def test_bot_chat_returns_string():
    with patch("core.bot.get_retriever"), \
         patch("core.bot.build_rag_chain") as mock_chain:

        mock_chain.return_value = MagicMock(return_value="Tokyo is great in spring!")

        from core.bot import TravelBot
        bot = TravelBot(session_id="test")
        answer = bot.chat("Best time to visit Tokyo?")

    assert answer == "Tokyo is great in spring!"


def test_bot_reset_clears_memory():
    with patch("core.bot.get_retriever"), \
         patch("core.bot.build_rag_chain") as mock_chain, \
         patch("core.bot.clear_session") as mock_clear:

        mock_chain.return_value = MagicMock(return_value="answer")

        from core.bot import TravelBot
        bot = TravelBot(session_id="reset-test")
        bot.reset()

    mock_clear.assert_called_once_with("reset-test")


def test_bot_memory_stores_messages():
    from core.memory import get_memory, clear_session

    mock_retriever = MagicMock()
    mock_retriever.invoke.return_value = [MagicMock(page_content="Hotels in Paris.")]

    with patch("core.bot.get_retriever", return_value=mock_retriever), \
         patch("core.chain.ChatGoogleGenerativeAI") as MockLLM:

        mock_llm = MagicMock()
        mock_llm.return_value = "Here are the hotels in Paris."
        MockLLM.return_value = mock_llm

        from core.bot import TravelBot
        bot = TravelBot(session_id="mem-bot-test")
        bot.chat("Hotels in Paris?")

    history = get_memory("mem-bot-test")
    assert len(history) == 2
    clear_session("mem-bot-test")
