# 텍스트 입출력은 기본 파일 입출력 방식.
# 실제로 application에서 객체나 json 형태로 파일 입출력한다.
# 객체 입출력은 pickle, marshal 모듈 사용
# JSON 전용 모듈인 json이 있다.


import json

data = {"name": "AI", "score": 95}

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("result.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data["name"], ":", loaded_data["score"])
