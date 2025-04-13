# ollama/ollama_runner.py

import subprocess

def run_ollama_prompt(prompt, model="mistral"):
    command = ["ollama", "run", model]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = process.communicate(input=prompt)
    return out.strip()
