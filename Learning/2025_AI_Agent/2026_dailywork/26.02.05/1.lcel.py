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

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 실력이 뛰어난 베테랑 번역가야, 입력된 문장을 한글로 번역해줘."),
    # sysyem = 역할(role)
    ("user","{input}")        
])

# (세번째 단계 : 출력파서 = 양식에 맞춰서 출력하는 것) <= 있을 수 있고 없을 수 있다
# - 모델의 응답값 중에서 문자열만 쏙 뽑아낼 수 있다
parser = StrOutputParser() # parser객체 생성(=객체도 변수의 한 종류다)

# (네번째 단계 : 체인생성 = 랭체인의 핵심 | 연결해서 사용한다는 것)
# - 입력 > 모델(서버) > 출력 순서
chain = prompt | model | parser # 서로 연결된 정보

# result = chain.invoke({"topic":"랭체인"})
result = chain.invoke({"input":"Learning LangChain is fun and easy for everyone"})
print(f"번역결과:{result}")