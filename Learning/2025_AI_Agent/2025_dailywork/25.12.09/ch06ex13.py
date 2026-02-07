from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
당신은 다이어트 전문 트레이너 입니다.
Tree-of-Thoughts 방식을 사용해 다음 문제를 해결하시오.
문제: '하루 30분밖에 운동할 시간이 없는 육아맘의 다이어트 시간표를 계획하십시오.'

규칙:
1단계(사고 생성): 서로 다른 관점에서 3개의 아이디어를 생성하라.
2단계(평가): 생성된 3개의 아이디어를 명확성, 실행 가능성, 차별성 기준으로 평가하라.
3단계(선택): 가장 높은 점수를 받은 아이디어 1개를 최종 선택하고, 선택 이유를 설명하라.

출력 형식:
[Thoughts]
1) ...
2) ...
3) ...

[Evaluation]
- 아이디어별 점수표(명확성/실행 가능성/차별성)
- 간단 평가 요약

[Best Choice]
- 선택된 아이디어:
- 선택 이유:
"""

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}]
)

print(resp.choices[0].message.content)
