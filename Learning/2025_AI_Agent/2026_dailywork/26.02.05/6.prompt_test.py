from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate 
   
import dotenv  
dotenv.load_dotenv() 

llm = OpenAI(temperature = 0.7)  

prompt = PromptTemplate(
    input_variabless=["topic"], #입력변수
    template = "다음 주제에 대해 간단히 설명해줘:{topic}"
)

chain1 = prompt | llm 
print("promptTemplate 결과:")
print(chain1.invoke({"topic":"인공지능"}))
print('==============================')



chat_prompt = ChatPromptTemplate.from_messages([
    ("system","너는 친절한 상담사야."), # system 고정 
    ("user","다음 주제에 대해 7살 어린이도 알기쉽게 예를 들어서 설명해줘: {topic}") #사용자의 구체적인 order
    
])

chain2 = chat_prompt | llm 
print("\n chatpromptTemplate 결과:")
print(chain2.invoke({"topic":"인공지능"}))

# user_input="오늘 날씨가 너무 좋아서 근처 공원에 산책을 하러 가고 싶어."
# result = chain.invoke({"korean_text":user_input})
# print(f"입력:{user_input}")
# print(f"결과:{result}")