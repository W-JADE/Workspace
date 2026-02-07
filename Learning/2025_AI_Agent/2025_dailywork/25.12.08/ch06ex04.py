'''
# 파일 생성 및 내용 쓰기
f = open("test_data.txt","w", encoding="utf-8") 

# 생성된 파일에 내용 쓰기
f.write("프롬프트 엔지니어링 실습 중")

# 열었으면 반드시 닫아야 한다.
f.close()
'''

# with open 구문을 이용한 자동 작성
with open("test_data.txt", "w", encoding="utf-8") as f:
    f.write("1, hong, 010-2222-1111\n") # 반복해서 사용할때 n
    f.write("1, min, 010-2222-2331\n")
    f.write("1, jang, 010-2222-5678\n")
print("파일 내용 읽기 완료")

'''
# with open 구문을 이용한 자동 종료
with open("test_data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
print("파일 내용 읽기 완료")
'''
