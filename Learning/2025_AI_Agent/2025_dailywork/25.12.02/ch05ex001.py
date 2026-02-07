# 함수 기초 다지기 
''''''
def hello(word) :
    # print((word + "\n")*2, end="")
    for i in range(3) :
        print(word)
        
# 선언된 함수를 호출한다
#hello("Hello")
# 다른 기능에 재활용 한다
#hello("world")
#print("Hi")

# 리스트를 확용한다
items = ["나비","잠자리","벌","거미","지렁이"]
for i in items :
    hello(i)