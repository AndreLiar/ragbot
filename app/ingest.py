# app/ingest.py

import os
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import pickle
from app import config

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            raw_text = page.extract_text()
            if raw_text:
                # Clean excessive line breaks, spaces, and fragmented words
                cleaned = (
                    raw_text
                    .replace("\n", " ")      # Remove line breaks
                    .replace("–", "-")        # Normalize dashes
                    .replace("  ", " ")       # Double space to single
                )
                text += cleaned + " "
    return " ".join(text.split())  # Final space normalization



def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def embed_and_index(chunks):
    model = SentenceTransformer(config.EMBEDDING_MODEL)
    embeddings = model.encode(chunks)
    
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)

    with open(os.path.join(config.FAISS_INDEX_DIR, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)

    faiss.write_index(index, os.path.join(config.FAISS_INDEX_DIR, "index.faiss"))

def run_ingest(pdf_filename):
    os.makedirs(config.FAISS_INDEX_DIR, exist_ok=True)
    pdf_path = os.path.join(config.PDF_UPLOAD_DIR, pdf_filename)
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    embed_and_index(chunks)
