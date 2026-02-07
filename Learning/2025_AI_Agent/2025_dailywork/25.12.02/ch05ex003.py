# 함수의 매개변수와 변환값(return)
# 매겨변수 parameter 또는 arguments라고 한다
# 반환값은 return value 라고 한다 
# 반환이란 말은 호출칸에 결과를 돌려준다는 것
def maximum(x,y) :
    if x>y :
        return x
    else :
        return y


a =20
b =4
maxNum = maximum(a,b)
print(f"{a}과 {b}중 더 큰 값은 {maxNum}이다.")
