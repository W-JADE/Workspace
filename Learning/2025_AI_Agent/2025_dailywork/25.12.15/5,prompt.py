#LLM 프롬프트 구조 실습하기_SNS 스타일 별 템플릿 프롬프트 고정해서 사용하기

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def main():
    platform = input("어떤 플랫폼을 이용하나요? (인스타그램/트위터/페이스북) : ")
    topic = input("주제를 정해서 알려주세요: ")
    tone = {"인스타그램":"감성톤","트위터":"직설톤","페이스북":"정보전달톤"}

    prompt = f"""
    다음 조건을 만족하는 SNS 글을 작성하시오.

    - 플랫폼: {platform}
    - 핵심 메시지: {topic}
    - 문체(톤): {tone}
    - 길이 2~3문장
    - 마지막 줄에 해시태그 5개
    - 출력 형식:
      1)입문 단계 해시태그 :
      2)중심주제의 해시태그 :
      3)감성/행동 해시태그 :

    각 항목은 번호를 붙여서 구분해 작성하시오.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "너는 SNS플랫폼 전문 인플루언스 관리자야"},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0
    )

    print("\n=== 생성된 광고 문구 ===")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
