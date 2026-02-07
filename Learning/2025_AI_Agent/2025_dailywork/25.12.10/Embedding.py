from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="서울 종로구 인구 자료를 분석하려 한다."
)

print(response.data[0].embedding[:10])  # 벡터 앞부분만 출력
