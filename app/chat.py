# app/chat.py

from app.retriever import search_similar_chunks
from ollama.ollama_runner import run_ollama_prompt

def build_prompt(context, question):
    with open("ollama/prompt_template.txt", "r") as f:
        template = f.read()
    return template.replace("{context}", context).replace("{question}", question)

def ask_question(question):
    chunks = search_similar_chunks(question)
    context = "\n\n".join(chunks)
    prompt = build_prompt(context, question)
    response = run_ollama_prompt(prompt)
    return response, context
