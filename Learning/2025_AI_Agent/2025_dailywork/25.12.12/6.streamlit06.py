from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("반가워 나는 LLM 챗봇A야")

if "messages" not in st.session_state :
    st.session_state["messages"] = []


for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.write(content)
    
user_input = st.chat_input("궁금한걸 입력해 주세요")

if user_input:
    st.session_state["messages"].append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신의 친절한 LLM 챗봇A 입니다."},
            *[
                {"role": role, "content": content}
                for role, content in st.session_state["messages"]
            ],
        ],
    )

    assistant_reply = response.choices[0].message.content

    
    st.session_state["messages"].append(("assistant", assistant_reply))
    with st.chat_message("assistant"):
        st.write(assistant_reply)
