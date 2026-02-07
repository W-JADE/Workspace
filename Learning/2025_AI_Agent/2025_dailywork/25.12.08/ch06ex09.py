# load_dotenv, os, openai 패키지 설치
from dotenv import load_dotenv
import os
from openai import OpenAI

# 키값 불러오기(load_dotenv사용)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# openai client생성 (openai생성)
client = OpenAI(api_key="api_key")


# 모델 호출 (client.chat.completions.create)
response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [
        {"role":"user","content":"안녕하세요 한줄로만 인사해줘요."}   
    ]
)
# 호출 결과 확인 (print response)
print(response.choices[0].message.content)

