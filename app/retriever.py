# app/retriever.py

import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from app import config

def search_similar_chunks(query, top_k=config.TOP_K):
    model = SentenceTransformer(config.EMBEDDING_MODEL)
    query_embedding = model.encode([query])

    index = faiss.read_index(os.path.join(config.FAISS_INDEX_DIR, "index.faiss"))
    with open(os.path.join(config.FAISS_INDEX_DIR, "chunks.pkl"), "rb") as f:
        chunks = pickle.load(f)

    _, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]
