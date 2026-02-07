# (첫단계 : 모듈 불러오기)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate #대화

# from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser    #문자형태 출력

# 1. api key 설정
import dotenv  # .env 파일을 읽기 위한 변수(환경변수) <- 이건 늘 앞에 작성
dotenv.load_dotenv() # 함수

# 2. 모델 (안정적인 gpt-4o-mini)
model = ChatOpenAI(model = "gpt-4o-mini",temperature=0.9)  
# 생성자 객제가 생성이 될때 자동으로 호출되는 함수


prompt = ChatPromptTemplate.from_template("네이버 뉴스 내용을 바탕으로 사람들의 클릭으 유도하는 '낚시성' 헤드라인 3가지를 만들어줘:{content}")     

chain = prompt | model 
news_content="AI가 적용됨에 따라 청년층의 실업률의 수치가 집계되었습니다."
# request(요청), response(응답), 

response = chain.invoke({"content":news_content}) # "" 안에는 문자열
print(response.content) 
# 응답객체명, 특정기명 -> 값을 불러온다. 
print('=========================')
print(response)