# 단일턴
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

while True :
    user_input = input("고객 :")
    
    if user_input == "exit" :
        break
    
    response = client.chat.completions.create(
        model= "gpt-4" ,    
        temperature=1.0,
        messages=[
            {"role":"system","content":"너는 고객을 응대하는 전문 상담사야"},
            {"role":"user","content":user_input}
            
        ],
    )
    
    print("AI:", response.choices[0].message.content)