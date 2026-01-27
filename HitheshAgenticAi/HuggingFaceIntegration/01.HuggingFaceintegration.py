# Connecting via Hugging Face open source models locally

from transformers import pipeline

pipe = pipeline("",model="gemma-3-270m-it")
pipe = pipeline("text-generation", model="google/gemma-3-270m-it")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)


