from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime

# 멋쟁이사자처럼 클럽의 새 회원을 등록하는 API를 만드세요. 
# 회원의 이름(str), 이메일(EmailStr), 그리고 등록 날짜(date)를 입력받아 등록합니다

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    registered_date: datetime

@app.post("/register/")
def register_user(user:User):
    return{"name":user.name, "email": user.email,"registered_date":user.registered_date}