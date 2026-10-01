import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a concise programming assistant."
        },
        {
            "role": "user",
            "content": "Explain what an API is in exactly two sentences."
        }
    ]
)

print("\n--- AI Response ---")
print(response.choices[0].message.content)
print("-------------------\n")