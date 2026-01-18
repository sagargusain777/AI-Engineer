from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai/"
)
#Zero Shot Prompting


response = client.chat.completions.create(

    model = "gemini-3-flash-preview",
    messages = [
        {"role":"system","content":"You have to only answer mathematical questions and If somebody ask you about anything else you just have to reply sorry i will not be able to answer"},
        {"role":"user","content":"Can you write a python code for binary search"}
    ]
)
print(response.choices[0].message.content)