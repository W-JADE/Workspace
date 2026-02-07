# try:
#     f = open("policy.txt","r")
#     print(f.read())
# except :
#     print("파일이 없습니다")
# finally :
#     print("예외 발생 유무와 상관 없이 실행됩니다")
#     if f :
#         f.close()
        
try:
    num = int(input("정수를 입력하세요: "))
    print(f"결과: {10 / num}")
except ValueError:
    print("입력값이 숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
finally:
    print("프로그램이 종료되었습니다.")