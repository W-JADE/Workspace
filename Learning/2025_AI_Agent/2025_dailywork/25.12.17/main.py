# 메인.py

from openai import OpenAI
from dotenv import load_dotenv
import os, json
import streamlit as st

from gpt_functions import get_busan_weather, tools

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(messages, tools=None):
    return client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
    )

st.title("Function Calling Chatbot")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "너는 도우미이다. 사용자가 오늘 날씨를 물어보면 get_busan_weather 도구를 사용하여 부산 날씨를 알려야 한다."
        }
    ]
for msg in st.session_state.messages:
    if msg["role"] in ("assistant", "user"):
        st.chat_message(msg["role"]).write(msg.get("content", ""))

if user_input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # 1차 호출: 필요 시 tool_calls 생성
    resp1 = get_ai_response(st.session_state.messages, tools=tools)
    msg1 = resp1.choices[0].message
    st.session_state.messages.append(msg1.model_dump())

    with st.expander("DEBUG: tool_calls (1차 응답)", expanded=False):
        st.json(msg1.tool_calls if msg1.tool_calls else "No tool_calls")

    # tool_calls 처리
    if msg1.tool_calls:
        for tc in msg1.tool_calls:
            tool_name = tc.function.name
            args = json.loads(tc.function.arguments or "{}")

            if tool_name == "get_busan_weather":
                result = get_busan_weather()

                tool_message = {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result
                }
                st.session_state.messages.append(tool_message)

                with st.expander("DEBUG: tool 실행 결과 (role='tool')", expanded=False):
                    st.write("tool_call_id:", tc.id)
                    st.write("tool_name:", tool_name)
                    st.write("arguments:", args)
                    st.write("result:", result)

        # 2차 호출: tool 결과를 반영해 최종 답변 생성
        resp2 = get_ai_response(st.session_state.messages, tools=tools)
        msg2 = resp2.choices[0].message
        st.session_state.messages.append(msg2.model_dump())
        st.chat_message("assistant").write(msg2.content)

    else:
        # tool 없이 바로 답한 경우
        st.chat_message("assistant").write(msg1.content)