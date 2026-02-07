# 전역변수(global)와 지역변수(local)
# 전역변수는 함수 외부에 선언되고 다른 모든 함수에서 접근 가능한 변수
# 지역변수는 함수 내부에 선언되고 함수 내부에서만 접근해서 사용하는 변수
# 함수는 자기 지역성이 있다
'''
#지역변수 설명
def funcA() :
    varA = 100 # 함수 내부에 있으니 지역변수
    print("varA의 값:", varA)

def funcB() :
    varB = 10
    print("varB의 값:",varB) # 다른 함수의 지역변수는 쓸 수 없음

funcA()
funcB()
'''

# 전역변수 설명
varC = 1000

def funcA() :
    global varC # global값은 상단에 있어야 출력됨
    varA = 100 # 함수 내부에 있으니 지역변수
    print("varA의 값:", varA)
    print("funcA에서 varC값", varC)
    varC = 3000

def funcB() :
    varB = 10
    print("funcC에서 varB값", varB) 
    print("funcB에서 varC값", varC)
funcA()
funcB()