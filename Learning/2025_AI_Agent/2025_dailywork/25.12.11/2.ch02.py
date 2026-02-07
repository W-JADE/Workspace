from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


prompt_stage1 = "고구마를 맛있게 조리하는 방법을 설명해줘"
prompt_stage2 = "고구마를 맛있게 조리하는 방법을 세가지 bullet형식으로 요약해줘"
prompt_stage3 = """
다음 예시처럼 bullet 구조를 유지해줘

예시:
- 조리법 1: 맛있는 고구마 선별법
- 조리법 2: 고구마를 맛있게 조리하는 방법

위 예시 스타일을 참고하여 고구마를 맛있게 조리하는 방법 세가지를 설명해줘
"""

prompts = [prompt_stage1, prompt_stage2, prompt_stage3]

MODEL_NAME ="gpt-4.1-mini"


for idx, p in enumerate(prompts, start=1):
    print(f"\n=== 단계 {idx} 출력 ===\n")
    print("입력 프롬프트:")
    print(p)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": p}],
        temperature=0.3
    )

    print("\n출력 결과:")
    print(response.choices[0].message.content)
    