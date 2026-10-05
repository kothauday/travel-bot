from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

from core.prompt import TRAVEL_PROMPT
from core.memory import get_memory, save_to_memory
from config import LLM_MODEL, GOOGLE_API_KEY, LLM_MAX_TOKENS


def _format_docs(docs) -> str:
    return "\n\n---\n\n".join(d.page_content for d in docs)


def build_rag_chain(retriever: VectorStoreRetriever, session_id: str):
    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        max_output_tokens=LLM_MAX_TOKENS,
    )

    def retrieve_and_format(inputs: dict) -> dict:
        docs = retriever.invoke(inputs["question"])
        history = get_memory(session_id)
        return {
            "context": _format_docs(docs),
            "question": inputs["question"],
            "chat_history": history,
        }

    chain = (
        RunnableLambda(retrieve_and_format)
        | TRAVEL_PROMPT
        | llm
        | StrOutputParser()
    )

    def run(question: str) -> str:
        answer = chain.invoke({"question": question})
        save_to_memory(session_id, question, answer)
        return answer

    return run
