# app.py
# app.py
import streamlit as st
from fileingestor import FileIngestor
from conversational import conversational_chat

st.title("Chat with PDF - 🦙 🔗")

uploaded_file = st.sidebar.file_uploader("Upload PDF file here", type="pdf")

if "history" not in st.session_state:
    st.session_state["history"] =[]

if uploaded_file:
    if "file_ingestor" not in st.session_state:
        st.session_state["file_ingestor"] = FileIngestor(uploaded_file)
    st.session_state["file_ingestor"].handlefileandingest()

user_input = st.text_input("Ask a question:", "")
if st.button("Send"):
    st.write(user_input)
    answer = conversational_chat(user_input)
    st.write("AI Response:", answer)