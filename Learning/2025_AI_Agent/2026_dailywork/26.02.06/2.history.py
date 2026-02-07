from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser   

import dotenv
dotenv.load_dotenv()

'''
from dotenv import load_dotenv
load_dotenv()
'''

model = ChatOpenAI(model = "gpt-4o-mini") 
prompt = ChatPromptTemplate.from_template("{input}")
chain = prompt | model | StrOutputParser() 

#첫번째 질문
print(f"질문1: 내 이름은 'jade'야 /응답:{chain.invoke({'input':'내 이름은 jade야'})}")
#두번째 질문
print(f"질문2: 내 이름이 뭔지 알고 있어? /응답:{chain.invoke({'input':'내 이름이 뭔지 알고 있어?'})}")

'''
질문1: 내 이름은 'jade'야 /응답:안녕하세요, Jade! 만나서 반갑습니다. 어떻게 도와드릴까요?
질문2: 내 이름이 뭔지 알고 있어? /응답:죄송하지만, 당신의 이름은 알지 못합니다. 이름을 알려주시면 좋겠습니다!
'''