import os
import streamlit as st

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from core.bot import TravelBot

st.set_page_config(
    page_title="Travel Bot",
    page_icon="✈️",
    layout="centered",
)

st.title("✈️ Travel Assistant")
st.caption("Ask me about destinations, hotels, flights, and travel packages.")


@st.cache_resource(show_spinner="Loading travel knowledge base...")
def load_bot():
    return TravelBot(session_id="streamlit-user")


bot = load_bot()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Options")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        bot.reset()
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.markdown("**Model:** Gemini 3.5 Flash Lite")
    st.markdown("**Embeddings:** HuggingFace (local)")
    st.markdown("**Knowledge base:** Travel data")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about travel destinations, hotels, flights..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = bot.chat(prompt)
            except Exception as e:
                answer = f"Something went wrong: {str(e)}"
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
