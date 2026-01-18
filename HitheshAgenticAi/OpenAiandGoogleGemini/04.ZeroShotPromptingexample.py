from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
	  api_key = os.getenv("GEMINI_API_KEY"),
		base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
				model="gemini-3-flash-preview",
				messages = [
						 {"role":"system","content":"You are advanced LLM Agent and you have to be very professional while answering computer science and engineering questions.You have to explain every bit of the question which is asked by the client"},
				         {"role":"user","content":"What is Zero Shot Prompting in System Prompt in field of AI"}
				])
				
print(response.choices[0].message.content)