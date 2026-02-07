from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

messages = [
    {"role": "system", "content": "당신은 친절한 Python 기초강의 선생님입니다 ."},
    {"role": "user", "content": "리스트와 튜플에 대해 이해하기 쉽게 코드 예시를 한가지 만들어 주세요."}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)