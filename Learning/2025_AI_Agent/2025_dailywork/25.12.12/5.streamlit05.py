# st.session_state
import streamlit as st

st.title("대화기록 유지 테스트 중!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("메시지 입력")

if st.button("추가"):
    st.session_state.messages.append(user_input)

st.write("대화 기록:")
for msg in st.session_state.messages:
    st.write("-", msg)