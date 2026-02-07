# st.text_input, st.text_area
import streamlit as st
st.title("반가워 나는 챗봇A야")

user_input= st.text_input("궁금한게 있으면 물어봐~")
user_prompt = st.text_area("자유롭게 원하는걸 질문해 줬으면 좋겠어")

st.write("응답 확인하기")
st.write(user_input)
st.write(user_prompt)