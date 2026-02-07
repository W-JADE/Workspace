# openAI 모듈 ApiKey 테스트
# openai 패키지 설치 가능
# 가상환경  > pip install openai

from openai import OpenAI

client = OpenAI(api_key="api_key")

response = client.responses.create(
    model = "gpt-5-nano",
    input = "오늘 경기도 고양시 일산동구의 날씨를 알려줘",
    store = True
)
print(response.output_text)