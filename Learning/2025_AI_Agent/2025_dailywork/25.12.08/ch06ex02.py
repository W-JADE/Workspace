# openai 와 python-dotenv 패키지를 먼저 설치해야한다.

from openai import OpenAI

client = OpenAI(api_key="api_key")

model = "gtp-4.1-mini"
message = [{
    "role" : "user",
    "content" :"안녕하세요 한줄로 인사해 주세요",
}]

responese = client.chat.completions.create(model="",messages=message)
print(responese.choices[0].message.content)

messages = [
    {"role": "system", "content": "당신은 친절한 Python 코딩 튜터입니다."},
    {"role": "user", "content": "리스트 평균을 계산하는 코드를 작성해줘."}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)