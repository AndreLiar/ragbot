# app/main.py

import streamlit as st
import os
from app import ingest, chat, config

st.set_page_config(page_title="Local RAG Chatbot 💬", layout="wide")
st.title("📄🤖 Local RAG Chatbot – PDF FAQ Assistant")

uploaded_file = st.file_uploader("Upload a PDF FAQ", type=["pdf"])
if uploaded_file:
    file_path = os.path.join(config.PDF_UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name}")
    
    with st.spinner("Indexing document..."):
        ingest.run_ingest(uploaded_file.name)
    st.success("✅ Document indexed!")

st.markdown("---")

question = st.text_input("Ask a question about your document:")
if question:
    with st.spinner("Thinking..."):
        response, context = chat.ask_question(question)

    st.markdown("### 🔍 Retrieved Context (Used for Answer)")
    st.code(context, language='markdown')

    st.markdown("### 💬 Answer")
    st.markdown(f"<div style='font-size:16px; line-height:1.6'>{response}</div>", unsafe_allow_html=True)
