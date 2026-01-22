from openai import OpenAI
import os
import json
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#Chain of Thought Prompting
system_prompt = """
You are an expern AI Assisatnat in resovling user queries using chain of thought algorithm.
You work on START , PLAN and OUTPUT steps.
 You need to first PLAN what needs to be done.The PLAN can be multiple strps.
 Once you think enough PLAN has been done, finally you give an OUTPUT.


 Rules:
 -Strictly Follow the given JSON output format
 -Only run on step at a time
 -The  sequence of steps is START(where user gives an input),PLAN(That
 can be multiple times) and finally OUTPUT(which is going to be displayed to user),

 Output JSON Format:
 {"step":"START"|"PLAN"|"OUTPUT","content":"string"}

 Example: 
  START : Hey can you solve 2+2+3*10/2
  PLAN :{"STEP":"PLAN","content": "Seems like user is intrested in mathematical question"}
   PLAN :{"STEP":"PLAN","content": "This mathematical question can be solve using BODMAS Rule"}
   PLAN :{"STEP":"PLAN","content": "So in that case we will divide first and it will be 2+2+3*5"}
   PLAN :{"STEP":"PLAN","content": "After that according to the bodmas rule after divide we will do multiplication 2+2+15"}
   PLAN :{"STEP":"PLAN","content": "Last step will be addition since we are left with additon symbols so it will be 19"}
   OUPTUT :{"STEP:":"OUPUT","content":"The output for the given mathematical expression is 19"}
   
   Important Rule 
   Only run one step at a time like dont just give the entire things in one go.
"""
response = client.chat.completions.create(
    model = "gemini-3-flash-preview",
    response_format = {"type":"json_object"},
    messages=[
        {"role":"system","content":system_prompt},
        {"role":"user","content":"What is the ouput for follwoing question 7+56+94+92-100/10*5"},
        {"role":"assistant","content":json.dumps({"step": "PLAN", "content": "The expression 7+56+94+92-100/10*5 will be solved by applying the order of operations, starting with division and multiplication followed by addition and subtraction."})},
        {"role":"assistant","content":json.dumps({"step": "PLAN", "content": "I will calculate the division part (100 / 10) and the multiplication part (result * 5) first, then proceed with the addition and subtraction from left to right to find the final result."})}
        ]

)
print(response.choices[0].message.content)