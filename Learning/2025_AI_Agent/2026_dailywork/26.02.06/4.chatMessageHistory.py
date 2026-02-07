from callfunction import*

from langchain_community.chat_message_histories import ChatMessageHistory # 대화기록을 관리해주는 클래스
from langchain_openai import OpenAI

llm = OpenAI(temperature=0.5)

history = ChatMessageHistory()

# 기능 => 함수(회사의 직원같은 느낌)

# 1. 매개변수 X  반환값 => 단순, 반복적인 일
# 2. 매개변수 O  반환값 X(보고X) = 데이터 저장 목적, 계산목적(재정 => 금액) Return X
# 3. 매개변수 O  반환값 O => 계산목적, return보고서
def show_history(): # def 함수명() or (매개변수):
    """현재까지의 대화 기록을 보기 좋게 5줄이내로 출력"""
    print("\n==대화기록==")
    
    # for 출력변수 in 출력대상자(=객체):
    for msg in history.messages: # 저장 데이터 출력
        # 구분
        role = "사용자" if msg.type == "human" else "AI"
        print(f"{role},: {msg.content}")        
    print("============\n")

def main():
    print("대화를 시작합니다.'exit'입력 시 종료됩니다.")
    while True :
        user_input = input(">>>")
        if user_input.lower() == "exit":
            print("프로그램을 종료합니다.")
            break
        # 사용자 메시지 기록
        history.add_user_message(user_input)
        
        # LLM 응답생성
        ai_resonse = llm.invoke(user_input)
        
        # AI 메시지 기록
        history.add_ai_message(ai_resonse)
        
        # 응답출력
        print(f"AI:{ai_resonse}")
        
        # 대화기록 출력
        show_history()
        
if __name__ == "__main__": # 
    main()
    print('__name__=>',__name__)