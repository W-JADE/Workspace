# list는 하나의 변수에 여러 항목을 저장하는데 사용된다


# 1. 기본 목록
music = ["좋은날","yuers","다리꼬지마"]
print(music)


# 2. 고정 번호 호출 : 순서는 0 부터 시작
scores = [80, 90, 100]
print(scores[0])  # 80 ← 첫 번째 점수
print(scores[1])   # 90 ← 두 번째 점수
print(scores[-1])  # 100 ← 뒤에서 첫 번째 점수(마지막)


# 3. 중복 항목 가능 
scores = [80, 90, 40, 90, 100]
print(scores)

# 4. 목록 길이 : len()
thislist = ["apple", "banana", "lemon" "cherry"]
print(len(thislist))

# 5. 반복문을 응용하기
fruits = ["사과", "바나나", "딸기"]

for f in fruits:
    print(f)
