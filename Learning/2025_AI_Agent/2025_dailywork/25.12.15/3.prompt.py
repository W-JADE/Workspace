# LLM 프롬프트 구조 실습하기_톤을 바꿔서 3가지 버전으로 만들어보기

# 감성적/전문적/유머러스 광고문구 만들기

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def main():
    product = input("제품명을 입력하세요: ")
    message = input("핵심 메시지를 입력하세요: ")
    tone = input("문체(톤)를 입력하세요: ")
    n = input("생성 개수를 입력하세요: ")

    prompt = f"""
    다음 조건을 만족하는 광고 문구를 생성하시오.

    - 제품명: {product}
    - 핵심 메시지: {message}
    - 문체(톤): {tone}
    - 출력 형식:
      1) 헤드라인(짧고 강렬하게)
      2) 보조 설명 1문장
      3) CTA 1문장
    - 생성 개수: {n}개

    각 항목은 번호를 붙여서 구분해 작성하시오.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "너는 광고 문구 생성 전문가야"},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0
    )

    print("\n=== 생성된 광고 문구 ===")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()