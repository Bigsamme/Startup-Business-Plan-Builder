from dotenv import load_dotenv
import os
from openai import OpenAI


ai_model = "gpt-4o-mini"


load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def generate():


    prompt = "What is the news today"

    chat = client.chat.completions.create(
        model = ai_model,
        messages=[
            {"role":"system","content":"You are a news reporter"},
            {"role":"user","content":prompt}
        ],
        max_tokens=500
    )
    return chat


print(generate())