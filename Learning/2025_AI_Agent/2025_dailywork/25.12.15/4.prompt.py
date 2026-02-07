# 프롬프트를 이용해서 숏츠의 구조 이해해보기

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def main():
    print("=== 유튜브 스크립트 기본구조 테스트 ===")

    topic = input("주제를 입력하세요:")
    tone = input("어떤 톤으로 설명해드릴까요?")

    prompt = f"""
    다음 형식을 따라 유튜브 영상 스크립트를 작성하시오.

    - 영상 길이: 30초
    - 주제: {topic}
    - 톤: {tone}
    
    [형식 조건]
    1) 도입: 1문장 (시청자 관심을 끄는 문장)
    2) 본론: 총 3문장 (핵심 메시지를 간결하게 설명, 진부하지 않게)
    3) 엔딩: 1문장 (마무리 + 다시 방문할 수 있도록 다음화 예고)
    
    """

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "너는 유튜브 영상 스크립트 제작 전문가야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    print("\n[유튜브 스크립트 결과]")
    print(resp.choices[0].message.content)

if __name__ == "__main__":
    main()