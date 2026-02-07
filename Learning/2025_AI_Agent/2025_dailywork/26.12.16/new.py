from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_streaming():
    question = input("===AI에게 질문하세요=== :")
    
    stream = client.chat.completions.create(
        model="gpt-4.1-mini",
        stream=True,
        messages=[
            {"role":"system","content":"당신은 국비지원교육 설명 담당자 입니다."},
            {"role":"user","content":question}]
    )
    
    print("\n[AI 응답 - 스트리밍 출력]")
    full_text = ""
    
    for chunk in stream :
        delta = chunk.choices[0].delta
        content = getattr(delta, "content", None)
        if content:
            full_text += content
            print(content, end="", flush=True)      
            
    with open("stream_output.txt","w",encoding="utf-8") as f :
        f.write(full_text)
        
if __name__ == "__main__" :
    chat_streaming()  
    
    
'''
=== 결과 ===
python으로 출력했을 때 결과
===AI에게 질문하세요=== : LLM리터러시 수업은 전국적으로 얼마나 진행되는지 퍼센트로 간단하게 알려줘

[AI 응답 - 스트리밍 출력]
현재 전국적으로 LLM 리터러시 수업은 약 25% 정도의 교육 기관에서 진행되고 있습니다. 추가로 궁금한 점 있으면 말씀해 주세요!

# stream_output.txt가 자동으로 생성되서 신규.py에서 물어본 AI응답을 저장해 준다
'''