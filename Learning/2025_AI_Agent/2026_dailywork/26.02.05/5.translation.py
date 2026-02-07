from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser   
import dotenv
  
dotenv.load_dotenv() # 함수

model = ChatOpenAI(model = "gpt-4o-mini")  # 클래스 -> 객체생성(목적 : 데이터 저장, 매서드 호출)

# 요약해줘 또는 몇 자이상, 몇b단어 이내로 간결하게 알려줘 => 긴 글 정리해주는 tip
prompt = ChatPromptTemplate.from_template(
    "다음 한국어 문장을 영어로 반역해줘, 반드시 10단어 이내로 간결하게 답해줘\n 문장 : {korean_text}"
)

chain = prompt | model | StrOutputParser() # 서로 연결된 정보

user_input="오늘 날씨가 너무 좋아서 근처 공원에 산책을 하러 가고 싶어."
result = chain.invoke({"korean_text":user_input})

print(f"입력:{user_input}")
print(f"결과:{result}")