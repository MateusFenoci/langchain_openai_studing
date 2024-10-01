from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model = "gpt-3.5-turbo",
    api_key=configure(),
)

messages = [
    {
        "role": "system",
        "content": "Você é um assistente que fornece informações sobre figuras históricas."
    },
    {
        "role": "user",
        "content": "Quem foi Alan Turing?"
    },
]

response = model.invoke(messages)

print(response)
print(response.content)