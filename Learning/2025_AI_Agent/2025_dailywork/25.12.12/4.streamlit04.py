# st.sidebar, st.columns
import streamlit as st

st.title("자! 이번엔 레이아웃을 구성해보자")

with st.sidebar:
    st.header("사이드바")
    model_name = st.selectbox("모델 선택", ["gpt-4.1-mini", "gpt-4.1", "gpt-4-nano"])
col1, col2 = st.columns(2)

with col1:
    st.write("왼쪽 영역")
    st.text_input("질문")

with col2:
    st.write("오른쪽 영역")
    st.write(f"선택한 모델: {model_name}")