from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate 
   
import dotenv  
dotenv.load_dotenv() 

llm = OpenAI(temperature = 0.5)  

# 구성요소 : system,user(=human massge),ai message
chat_prompt = ChatPromptTemplate.from_messages([
    ("system","너는 팩트를 잘 말해주는 기업채용전문 담당자야."), # system 고정 
    ("user","AI 에이전시 취업준비생에서 {topic}에 대해 냉혹한 현실을 3줄로 요약해서 정리해줘."), #사용자의 구체적인 order
    ("ai","알겠습니다. 현실을 반영해서 냉정하고 논리적으로 팩트를 정리해 설명해드리겠습니다.")
])

chain = chat_prompt | llm 
# print("\n chatpromptTemplate 결과:")
print(chain.invoke({"topic":"취업시장 스팩"}))

