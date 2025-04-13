

```markdown
# 📄🤖 Local RAG Chatbot – Insurance FAQ Assistant

A fully local Retrieval-Augmented Generation (RAG) chatbot that answers questions from internal PDF documents (like insurance FAQs) using **Ollama**, **Mistral**, **FAISS**, and **Streamlit**. No API keys or internet required — runs 100% locally.

---

## 🚀 Features

- 🔍 PDF ingestion + semantic chunking
- 🧠 Local embedding & vector search via FAISS
- 💬 Natural Q&A with contextual answers using Mistral
- 🧾 Justifies each response with reasoning based on source content

---

## 🛠️ Stack

- Python 3.12 (via Conda)
- [Streamlit](https://streamlit.io/)
- [SentenceTransformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Ollama](https://ollama.com/) (Mistral model)

---

## 📦 Setup

### 1. Install dependencies

```bash
git clone https://github.com/AndreLiar/ragbot.git
cd ragbot

conda create -n ragbot python=3.12.7 -y
conda activate ragbot

pip install -r requirements.txt
```

### 2. Pull the model

```bash
ollama pull mistral
```

### 3. Run the app

```bash
export PYTHONPATH=.
streamlit run app/main.py
```

---

## ✅ How It Works

1. Upload a PDF (e.g., insurance FAQs)
2. The system extracts + chunks the content
3. Embeds chunks and builds FAISS index
4. Ask your question
5. The bot retrieves relevant content, forms a prompt, and generates a grounded response using Mistral

---

## 💬 Example Q&A

> **Q:** What is a deductible in insurance?

**A:** A deductible is the amount the insured must pay out of pocket before insurance coverage begins.

**Reason:** This is directly stated in the document under general insurance terms, explaining how deductibles shift initial costs to the policyholder.

---

## 🧪 Next Improvements

- Highlight source context
- Support multiple PDFs
- Add CSV export of Q&A
- Chunk metadata tracing (page, section, etc.)



