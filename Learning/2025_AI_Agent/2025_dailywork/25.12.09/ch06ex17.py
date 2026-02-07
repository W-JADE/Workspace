import json

try:
    with open ("config.json","r",encoding="utf-8") as f:
        config = json.load(f)
    print("저장 된 파일 업로드 완료:", config)
except FileNotFoundError :
    print("config.json 파일이 존재하지 않습니다.")
except json.JSONDecodeError :
    print("JSON 형식이 잘못 되었습니다.")
finally:
    print("작업이 완료되었습니다. 감사합니다.")