# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/public", StaticFiles(directory="public", html=True), name="public")

@app.get("/")
def root(message: str = "초등학생용 사칙연산 계산기") :
    print("GET - / 요청 받았다!")
    return {
        "message": message,
    }

# 서버에서 사칙연산 계산기 구현해보기
# path parameter - /연산자/{}/{}(항1/항2) 
# 우아한 URL
@app.get("/plus/{a}/{b}")
def plus(a:int,b:int):
    print("더하기 결과확인 =>",a, b, a+b)
    return a + b

@app.get("/min/{a}/{b}")
def plus(a:int,b:int):
    print("빼기 결과확인 =>", a, b, a-b)
    return a - b

@app.get("/mult/{a}/{b}")
def plus(a:int,b:int):
    print("곱하기 결과확인 =>",a, b, a*b)
    return a * b

@app.get("/div/{a}/{b}")
def plus(a:int,b:int):
    print("나누기 결과확인 =>",a, b, a/b)
    return a / b