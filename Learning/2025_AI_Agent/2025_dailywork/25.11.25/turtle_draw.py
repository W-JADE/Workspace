# 스파이럴 모양의 그래프를 만드는 방법 : turtle

import turtle as t 

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup(); t.goto(-150, 0); t.pendown()
t.speed(0)
length = 5
for _ in range(100):
    t.forward(length)
    t.right(89)
    length += 5

t.done()