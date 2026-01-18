from openai import OpenAI

client = OpenAI(
    api_key ="",
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(

    model ="gemini-3-flash-preview",
    messages = [{
        "role": "user",
        "content": "Why are we learning openai call using gemini"
    }]
)
print(response.choices[0].message.content)