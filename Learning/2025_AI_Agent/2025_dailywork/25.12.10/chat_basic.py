from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role":"user","content":"당신은 데이터 통계 박사입니다."},
        {"role":"user","content":"대한민국 3인 가구의 평균 식비를 알려주세요"}
    ]
)

print(response.choices[0].message.content)