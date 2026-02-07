from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

text = "서울시는 대한민국의 수도입니다."

embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

print(embedding.data[0].embedding[:10])
