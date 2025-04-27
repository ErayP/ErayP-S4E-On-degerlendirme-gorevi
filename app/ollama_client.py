import os
import json
import re
import requests
from typing import TypedDict

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3:latest")

class GenerationResult(TypedDict):
    title: str
    code: str

def generate_code(prompt: str) -> GenerationResult:
    system_prompt = (
        "You are a code generation assistant. "
        "Only respond with valid JSON in a single line, "
        "with exactly two keys: \"title\" and \"code\". No extra text."
    )
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt}
        ],
        "stream": False
    }

    resp = requests.post(f"{OLLAMA_URL}/v1/chat/completions", json=payload)
    resp.raise_for_status()
    raw = resp.json()["choices"][0]["message"]["content"]


    clean = re.sub(r"```(?:json|python)?\s*", "", raw).replace("```", "").strip()

    # —————— JSON parse aşamaları ——————
    try:
        data = json.loads(clean)
    except json.JSONDecodeError:
        # Fallback: İlk `{` ile son `}` arasını al
        start = clean.find("{")
        end   = clean.rfind("}") + 1
        if start == -1 or end == 0:
            raise ValueError(f"No JSON object found in:\n{raw}")
        snippet = clean[start:end]
        data = json.loads(snippet)

    # —————— Sonuç üret ——————
    return GenerationResult(title=data["title"], code=data["code"])


if __name__ == "__main__":
    # Kullanıcı prompt’u
    result = generate_code("iki sayıyı toplayan fonksiyon")

    # Ekrana bastır
    print("Başlık:", result["title"])
    print("Kod:\n" + result["code"])
