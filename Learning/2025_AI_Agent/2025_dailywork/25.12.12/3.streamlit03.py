# st.button
import streamlit as st

st.title("이번 시간은 버튼 트리거가 어떻게 출력되는지 확인할거야")

prompt = st.text_input("질문을 입력헤줘")

if st.button("LLM 호출 버튼입니다") :
    st.write("무엇을 도와드릴까요?")
    st.write(f"입력한 질문 : {prompt}")