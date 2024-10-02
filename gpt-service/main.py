import os
from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.post("/ask_me_anything")
async def ask_me_anything(question: str):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
