# LLM 프롬프트 구조 실습하기_Format의 형태를 수정해서 테스트해보기

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

topic = input("설명할 주제를 입력하세요: ")

formats = {
    "문장형": "2문장으로 요약해서 설명하세요",
    "목록형": "bullet 목록으로 3줄 이내로 설명하세요.",
    "표 형식": "선택한 내용을 4열 표 형식으로 정리하세요. (항목 | 종류 | 설명 | 선호도)",
    "JSON": " 다음 결과의 핵심 포인트를 JSON 형식으로 출력하시오. { '요약': '', '장점2개 단점 2개': [] }",
}
for fmt_name, fmt_instruction in formats.items():
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "출력 형식을 정확하게 인지해서 출력하는 AI 입니다."},
            {"role": "user", "content": f"{topic}를 {fmt_instruction}"}
        ]
    )

    print(f"\n=== Format: {fmt_name} ===")
    print(resp.choices[0].message.content)
