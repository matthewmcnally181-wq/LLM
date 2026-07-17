from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

class Prompt(BaseModel):
    message: str

@app.post("/chat")
def chat(prompt: Prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "prompt": prompt.message,
        "stream": False
    })

    data = response.json()
    return {"response": data["response"]}