# LLM 프롬프트 구조 실습하기_역할을 추가해서 변형해보기

from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. 환경 변수 로드 및 클라이언트 생성
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY가 설정되지 않았습니다.")

client = OpenAI(api_key=api_key)


def ask_question():
    print("===일반 질의응답 기능입니다.===")
    question = input("\n[질문] 내용을 입력하세요:\n> ")
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 친절한 질의응답 도우미입니다."},
            {"role": "user", "content": question},
        ],
    )
    print("\n[질문 응답]")
    print(resp.choices[0].message.content)


def summarize_text():
    print("===텍스트 요약 기능입니다.===")
    text = input("\n[요약] 텍스트를 입력하세요:\n> ")
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 전문 요약 도우미입니다."},
            {"role": "user", "content": f"다음을 3줄로 요약하시오:\n{text}"},
        ],
    )
    print("\n[요약 결과]")
    print(resp.choices[0].message.content)


def rewrite_sentence():
    print("===문장 기사 스타일 변환 기능입니다.===")
    question = input("\n[기사 스타일 변환] 문장을 입력하세요:\n> ")

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "당신은 정확하고 객관적으로 기사를 작성하는 전문 뉴스 기자입니다. "
                    "주어진 문장을 뉴스 기사 스타일로 재구성하십시오. "
                    "불필요한 수식어 및 감탄사 제거"
                ),
            },
            {
                "role": "user",
                "content": f"다음 문장을 전문 뉴스 기사 스타일로 재작성하시오:\n{question}",
            },
        ],
    )

    print("\n[기사 스타일 변환 결과]")
    print(resp.choices[0].message.content)


def main():
    while True:
        print("\n=== AI 리포터 챗봇기자 구현 테스트 ===")
        print("1. 일반 질의응답")
        print("2. 텍스트 요약")
        print("3. 문장 기사 스타일 변환")
        print("0. 종료")

        choice = input("메뉴 번호를 선택하세요: ")

        if choice == "1":
            ask_question()
        elif choice == "2":
            summarize_text()
        elif choice == "3":
            rewrite_sentence()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()

