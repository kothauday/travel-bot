from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SYSTEM_PROMPT = """You are a knowledgeable and friendly travel assistant.
Use the context below — retrieved from our travel knowledge base — to answer the user's question accurately.
If the context does not contain enough information, say so honestly and offer general travel advice.

Context:
{context}
"""

TRAVEL_PROMPT = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}"),
])
