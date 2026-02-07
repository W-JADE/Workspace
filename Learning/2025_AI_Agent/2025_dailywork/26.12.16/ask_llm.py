#3. 위 '1실습'과 같은 방식으로 함수를 재구성해서 import한다

from dotenv import load_dotenv
from openai import OpenAI
import time
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str,
            model: str = "gpt-4o-mini",
            temperature: float = 0.3,
            max_retries: int = 3,
            retry_delay: float = 2.0) -> str:
    """LLM 호출에 대한 기본 함수로, 예외 처리와 재시도 로직을 포함합니다."""
    for attempt in range(1, max_retries + 1):
        print("====답변===:",attempt)
        try:
            # a = max_retries / attempt # 강제 오류 발생장치
            resp = client.chat.completions.create(
                model=model,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return resp.choices[0].message.content
        except Exception as e:
            print(f"[오류 발생] 시도 {attempt}/{max_retries}: {e}")
            if attempt == max_retries:
                return "죄송합니다. 현재 AI 응답을 가져오는 데 실패했습니다. 잠시 후 다시 시도해 주세요."
            time.sleep(retry_delay)