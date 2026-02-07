# (첫단계 : 모듈 불러오기)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate #대화
from langchain_core.output_parsers import StrOutputParser    #문자형태 출력

# (두번쨰 단계 : api key 설정 및 모델 설정하기)
# 1. api key 설정
import dotenv  # .env 파일을 읽기 위한 변수(환경변수) <- 이건 늘 앞에 작성

dotenv.load_dotenv() # 함수

# 2. 모델 (안정적인 gpt-4o-mini)
model = ChatOpenAI(model = "gpt-4o-mini")  # 클래스 -> 객체생성(목적 : 데이터 저장, 매서드 호출)
# print("model=>", model) # 메모리에 공간이 잡히는지 확인하기 ex)주소값(=집주소)

prompt1 = ChatPromptTemplate.from_template("{item} 을 활용한 혁신적인 미디어콘텐츠 아이디어를 하나 제안해줘.")
prompt2 = ChatPromptTemplate.from_template("다음 아이디어의 예상되는 기술적 문제적을 2가지 알려줘:{idea}")

chain1 = prompt1 | model | StrOutputParser() 
chain2 = prompt2 | model | StrOutputParser()

# 첫번째 실행
idea = chain1.invoke({"item":"홀로그램"})
print(f"아이디어:{idea}\n")

# 두번쨰 실행
problems = chain2.invoke({"idea":idea})
print(f"예상 문제점: \n{problems}")