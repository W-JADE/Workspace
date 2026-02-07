from openai import OpenAI
from dotenv import load_dotenv
import os

# 1) 환경 변수에서 OPENAI_API_KEY를 불러옵니다.
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2) Assistant를 생성합니다.
assistant = client.beta.assistants.create(
    name="서울시 인구 전문가",
    instructions=(
        "당신은 서울시 각 구별 인구 통계를 설명하는 전문가입니다. "
        "사용자가 전달하는 숫자 데이터를 바탕으로, 이해하기 쉬운 한국어로 "
        "요약·해석·비교 설명을 해 주세요."
    ),
    model="gpt-4.1-mini",
)

print("Assistant id:", assistant.id)
