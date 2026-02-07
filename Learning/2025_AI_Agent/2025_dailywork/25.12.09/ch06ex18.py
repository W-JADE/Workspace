from datetime import datetime
import traceback

CHAT_LOG = "chat_log.txt"
ERR_LOG = "error.log"

def now() -> str :
    return datetime.now().isoformat(timespec="seconds")

def append_chat_log(role: str, text: str) -> None:
    line = f"{now()} | {role.upper()} | {text}\n"
    with open(CHAT_LOG, "a", encoding="utf-8") as f:
        f.write(line)

def log_exception(exc: BaseException) -> None:
    header = f"{now()} | {type(exc).__name__} | {exc}"
    stack = traceback.format_exc()
    with open(ERR_LOG, "a", encoding="utf-8") as f:
        f.write(header + "\n")
        f.write(stack + "\n")

def generate_reply(user_text: str) -> str:
 
    preview = user_text.strip().replace("\n", " ")
    if len(preview) > 50:
        preview = preview[:50] + "..."
    return f"요청을 확인했다. 핵심은 다음과 같다: {preview}"

def main() -> None:
    print("프롬프트 로그 기록기 시작(종료: 빈 입력 후 Enter).")
    while True:
        try:
            user = input("USER> ").strip()
            if user == "":
                print("종료한다.")
                break

            append_chat_log("user", user)
            reply = generate_reply(user)

            append_chat_log("assistant", reply)
            print(f"ASSISTANT> {reply}")

        except Exception as e:

            log_exception(e)
            print("오류가 발생했으나 계속 진행한다. 상세는 error.log 참조.")

if __name__ == "__main__":
    main()
