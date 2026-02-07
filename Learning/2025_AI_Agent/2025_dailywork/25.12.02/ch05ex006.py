# 도전 문제
# menu() 함수에서 no변수에 새 값을 입력받고,
# run() 함수에서 입력받은 값을 확인하기
    
no = 0

def menu():
    global no    # 전역변수 사용
    # pass는 기재하지 않음_내역이 추가되면 빈 값이 아니라서 기재X
    # 전역변수(global 함수로 구현) no에 새 값 입력
    no = int(input("입력할 no 값은?: "))
    
def run():
    print("no 변수의 값은? :", no)
    # pass
    # no 변수의 값 출력

while no != 6:
    menu()
    run()

print("END")