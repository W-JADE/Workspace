# mini_agent_structure.py

from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로드입니다.
load_dotenv()

client = OpenAI()

prompt = """
당신은 세 단계의 역할을 순차적으로 수행합니다.

1단계: 아이디어 플래너입니다.
신제품 홍보 영상을 위한 기획안을 5단계 구조로 작성하시오.

2단계: 콘텐츠 생성기입니다.
1단계에서 작성한 기획안을 기반으로 30초 분량의 스크립트를 작성하시오.

3단계: 톤 수정기입니다.
2단계에서 작성한 스크립트를 고객 친화적이고 명확한 톤으로 다듬으시오.

역할 수행은 순차적으로 진행하며 각 단계의 결과를 모두 출력하시오.
"""

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    n=2
)

print("=== 미니 에이전트 구조 출력 결과 ===\n")
print(response.choices[0].message.content)
