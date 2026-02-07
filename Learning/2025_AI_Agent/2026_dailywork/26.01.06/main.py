from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from datetime import datetime
import csv

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(
        "join-us.html",
        {"request": request}
    )
@app.post("/join", response_class=HTMLResponse)
def submit_form(
    request: Request,
    name: str = Form(...),
    age: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    gender: str = Form(...)
):
    print(">>> [POST] - /join", name,address,age,email,phone,gender)
    
    # CSV파일로 저장
    CSV_FILE = "person.csv"
    with open(CSV_FILE, "a+", newline="", encoding="utf-8") as f:
        f.seek(0)
        first_line = f.readline().strip()
        writer = csv.writer(f)
        
        if not first_line:
            writer.writerow(["submitted_at", "name", "address", "phone", "email", "age", "gender"])
        writer.writerow(["submitted_at", name, address, phone, email, age, gender])
    
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "name": name,
            "age": age,
            "address": address,
            "phone": phone,
            "email": email,
            "gender": gender
        }
    )
    
    # return HTMLResponse("""
    #     <!DOCTYPE html>
    #     <html>
    #         <body>
    #             <h1>결과 페이지</h1>
    #             <ul>
    #                 <li>성명 : {name}<li>
    #                 <li>주소 : {adress}<li>
    #                 <li>이메일 : {email}<li>
    #             <ul>
    #         </body>
    #     </html>
    # """)