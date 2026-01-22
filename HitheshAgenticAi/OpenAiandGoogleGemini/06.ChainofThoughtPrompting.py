from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()


client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai/"
)


#Defining the system prompt
system_prompt =  """
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
   You MUST reply with ONLY a valid JSON object.
       No markdown.
       No explanation.
       No text outside JSON
"""

message_history = [
                        {"role":"system","content" : system_prompt},
                 ]

user_query= input(" What are you looking for today ? 😇")
message_history.append({"role":"user","content":user_query})
  
while True:

        response = client.chat.completions.create(
                model = "gemini-3-flash-preview",
                response_format= {"type":"json_object"},
                messages = message_history
         )

        query_result = response.choices[0].message.content
        message_history.append({"role":"assistant","content":query_result})

        parsed_result = json.loads(query_result)
        if parsed_result.get("step")== "START":
              print("🧠"+parsed_result.get("content"))
              continue
        if parsed_result.get("step")== "PLAN":
              print("🤖"+parsed_result.get("content"))
              continue
        if parsed_result.get("step")=="OUTPUT":
              print("💼"+parsed_result.get("content"))
              break 

