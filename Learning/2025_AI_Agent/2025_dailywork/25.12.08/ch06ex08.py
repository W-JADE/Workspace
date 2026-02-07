import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FACTCHAT_API_KEY")

API_URL = "https://factchat-cloud.mindlogic.ai/v1/api/anthropic/messages"

def ask_llm(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }

    data = {
        "model": "claude-sonnet-4-5-20250929",   # ✔ 올바른 모델명
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    answer = ask_llm("AI Agent 개발에 필요한 핵심 기술을 한 문단으로 요약해줘.")
    print(answer)
