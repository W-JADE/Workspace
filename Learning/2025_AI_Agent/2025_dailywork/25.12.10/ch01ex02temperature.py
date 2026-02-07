from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

question = "15개월 아기 놀이방법을 3가지 추천해줘(2줄로 요약하세요)"
model = "gpt-4.1-mini"
messages = [{"role": "user", "content": question}]

for temp in [0, 0.7, 1.2]:
    print("\n::::", temp, "::::")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temp
    )
    print(response.choices[0].message.content)
