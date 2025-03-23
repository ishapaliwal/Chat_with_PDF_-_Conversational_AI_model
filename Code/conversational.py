# conversational.py
import streamlit as st

def conversational_chat(query):
    result = st.session_state["chain"](
        {"question": query, "chat_history": st.session_state["history"]}
    )
    st.session_state["history"].append((query, result["answer"]))
    return result["answer"]