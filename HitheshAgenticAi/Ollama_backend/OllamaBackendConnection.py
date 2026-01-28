
from fastapi import FastAPI,Body
from ollama import Client

app = FastAPI()

client = Client(
    host = "http://localhost:11434/"
)


@app.post("/userquery")   
def queryMessage(usermessage : str = Body(...,description="message")):
    response = client.chat(
        model = "qwen3:8b",
        messages = [
            {"role":"user","content": usermessage}
            ]
        )
    return {response.message.content}