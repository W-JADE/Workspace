# 직접 해보기
# 두 정수를 입력받아서 합한 결과를 반환하는 함수 add(x,y)를 구현하기

x = 3
y = 5
def add(x,y) :
    # return x+y #return 뒤에 들어가는 값(sum_value)은 호출하는 값
    # s = x + y
    return x, y, x+y
sum_value = add(x, y)
print(f"{x} + {y} = {sum_value}")


