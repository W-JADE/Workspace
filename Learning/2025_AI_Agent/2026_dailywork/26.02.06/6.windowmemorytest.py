from callfunction import*
from langchain_core.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferWindowMemory

llm = ChatOpenAI(model = "gpt-4o-mini") 

memory =  ConversationBufferWindowMemory(K=3,return_messages=True) # 이전 대화를 메세지 형대로 확인되는 것

prompt = ChatPromptTemplate.from_messages([
    ("system","당신은 여행 전문가야. 사용자의 질문에 친절히 답변해줘."),
    MessagesPlaceholder(variable_name="history"), # chat_history라는 변수에 들어있는 다양한 메세지들을 이 위치에 넣어준다
    ("human","{input}") 
])
chain = prompt | llm

inputs=["제주도 여행지를 추천해줘","서귀포시에서 핫한 여행지는 어디애?","그럼 그 근처 맛집은 어디야?"]

for user_input in inputs:
    history = memory.load_memory_variables({})["history"]
    # 메모리에 저장된 값을 꺼내라(매개변수값 -> 입력받은 값)
    
    result = chain.invoke({"history":history,"input":user_input})
    
    print(f"\n사용자:{user_input}\n응답:{result.content}")
    memory.save_context({"input": user_input}, {"output": result.content})