# from callfunction import ChatOpenAI,ChatPromptTemplate,StrOutputParser 이렇게 작성도 가능
# from 모듈명
from callfunction import* # 모듈 내 들어가 있는 모든 요소 *로 표시
# 다른 모듈
from langchain_core.prompts import MessagesPlaceholder # 여러 메세지를 넣어주는 역할
from langchain_core.messages import HumanMessage,AIMessage

# 1. 모델 설정
model = ChatOpenAI(model = "gpt-4o-mini") 

# 2. 프롬프트 설계
prompt = ChatPromptTemplate.from_template([
    ("system","너는 사용자의 이전 대화를 기억하는 전문 AI 비서야."),
    MessagesPlaceholder(variable_name="chat_history"), # chat_history라는 변수에 들어있는 다양한 메세지들을 이 위치에 넣어준다
    ("user","{input}") # 현재 사용자 입력자리
])
chain = prompt | model | StrOutputParser() 

# 대화 기록 저장 리스트 -> exit 문자열을 만나기 전까지 계속 저장한다
chat_history =[] #humanmassage,aimessage
#대화 기록 저장 리스트->exit문자열을 만나기 전까지 계속해서 저장
chat_history = [] #HumanMessage,AIMessage

print("대화를 시작합니다. 종료할려면 exit를 입력요망")
while True:  #들여쓰기=>제어문과 함수, 클래스 작성할때 자동으로 들여쓰기가 필요
    user_input = input("사용자: ") #input함수 이용
    
    if user_input.lower() == "exit":  # "exit" 객체명.호출할 메서드명() =>파이썬에서는 모든것이 거의 객체입니다.(문자열도 객체다)
        break #탈출문
    response = chain.invoke({
        "input":user_input, #현재 질문
        "chat_history":chat_history #이전 대화 전체 전달
    })
    print("AI:",response) 
    
    #대화기록 누적=>사용자가 물어보는 질문과 AI 대답하는 문자열을 구분해서 저장=>꺼내올때도 구분해서 받아올 수 있다.
    Hu = HumanMessage(content=user_input)
    chat_history.append(Hu)
    
    Ai = AIMessage(content=response)
    chat_history.append(Ai)
    
    #chat_history.append(HumanMessage(content=user_input)) #축약형(익명객체형태로 값을 저장시킨 방법) it is->it's
    #chat_history.append(AIMessage(content=response))
