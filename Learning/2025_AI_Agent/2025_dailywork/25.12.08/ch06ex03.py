from openai import OpenAI

client = OpenAI(api_key="api_key")

with open("prompt.txt","r",encoding="utf-8") as f :
    prompt = f.read()
    
messages = [
    {"role": "system", "content": "당신은 데이터 분석을 가르치는 교수입니다."},
    {"role": "user", "content": prompt}
]



response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=messages
)

print(response.choices[0].message.content)