from unittest.mock import patch, MagicMock
from core.retriever import get_retriever


def test_get_retriever_returns_retriever():
    mock_store = MagicMock()
    mock_store.as_retriever.return_value = MagicMock()

    with patch("core.retriever.get_vector_store", return_value=mock_store):
        retriever = get_retriever()

    mock_store.as_retriever.assert_called_once()
    assert retriever is not None


def test_retriever_uses_mmr():
    mock_store = MagicMock()

    with patch("core.retriever.get_vector_store", return_value=mock_store):
        get_retriever()

    call_kwargs = mock_store.as_retriever.call_args.kwargs
    assert call_kwargs["search_type"] == "mmr"
