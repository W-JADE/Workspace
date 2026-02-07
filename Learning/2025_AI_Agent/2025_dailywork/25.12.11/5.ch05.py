# 멀티턴
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=1.0,
        messages=messages,
    )
    return response.choices[0].message.content 
messages = [
    {"role": "system", "content": "너는 고객의 고민을 해결해주는 전문 상담가야."}
]

while True :
    user_input = input("고객: ")
    
    if user_input == "exit" :
        break
    
    messages.append({"role": "user", "content": user_input})  
    ai_response = get_ai_response(messages) 
    messages.append({"role": "assistant", "content": ai_response})  

    print("AI:", ai_response)    