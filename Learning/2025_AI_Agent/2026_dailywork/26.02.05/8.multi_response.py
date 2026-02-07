from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate 
   
import dotenv  
dotenv.load_dotenv() 
# 모듈을 직접 만들어서 불어와 사용(=사용자 정의 모듈 작성)

llm = OpenAI(temperature = 0.5)  
# systemMessage -> 모델의 성격, 역할, 규칙의 정의
# usermessage -> 모델의 응답 톤이나 기본 답변 스타일 지정

# 구성요소 : system,user(=human massge),ai message
chat_prompt = ChatPromptTemplate.from_messages([
    ("system","당신은 급매 전문 부동산 공인중개사야."), # system 고정 
    ("user","26년 5월9일 이전으로 나오는 {APT}에 대한 시장조사를 해보자."), #사용자의 구체적인 order
    ("ai","알겠습니다. 실제 데이터를 반영해서 시장조사를이 정리해보겠습니다."),
    ("user","6억 이하의 매물중 {APT}가 많이 나오는 지역 3군데를 알려줘!") #[], SET={}
])

chain = chat_prompt | llm 
# print("\n chatpromptTemplate 결과:")
print(chain.invoke({"APT": "아파트 급매"}))

