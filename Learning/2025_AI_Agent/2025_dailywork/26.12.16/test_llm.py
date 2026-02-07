# 1. test_llm.py 파일을 먼저 만든다

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str,
            model: str = "gpt-4.1-mini",
            temperature: float=0.7)->str:
    
    resp = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=
        [{"role":"user","content":prompt}]        
    )
    return resp.choices[0].message.content