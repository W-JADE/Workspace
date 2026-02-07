# 난수 발생기 심화 문제 풀기 (게임!)
import random

while True : # 반복루프
    print("::: 높다 낮다 게임 :::") 
    
    num = random.randint(1,100) # 1~99 사이 랜덤 숫자
    # num = random.choice([1,3,5]) # 리스트의 항목 중 랜덤으로 선택
    #시스템이 발생시킨 난수를 5번 시도 내에 맞추기 (높다,낮다 게임 같음)
    min = 1
    max = 100
    num = random.randint(min,max)
    count = 5
    
    while count > 0 :
        # 1. 사용자 입력
        user_num = int(input(f"사용자 입력 {min}~{max} 사이 :"))
        
        # 2. 사용자 입력값과 num 같은지 비교 (틀리면 종료)
        if user_num == num :
            print("훌륭해요! 정답입니다!")
            break
        
        # 3. 다르다면 min, max 범위를 다시 입력하기
        elif user_num < num :
            print("더 높은 값을 제시하세요!")
        else :
            print("조금 더 낮은 값을 제시하세요")
                
        count -= 1
    
    if count == 0 :
        print("게임 실패")
        print(f"정답은({num})입니다")

    tryagain = input("재시도 하시겠습니까? (Y/N) : ")
    # 다시 처음부터 실행 되는지 확인해보기
    
    if tryagain.lower() != "y" : # 대소문자 구분 (.lower)
        print("END")
        break
    
    