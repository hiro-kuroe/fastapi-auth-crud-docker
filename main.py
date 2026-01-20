import os

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
import socket
from db.base import Base
from db.session import engine, get_db, SessionLocal
from crud.user import get_user_by_username
from utils.security import verify_password, get_password_hash, get_current_user
from db.models.user import User
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



app = FastAPI()

@app.on_event("startup")
def create_demo_user():
    db = SessionLocal()
    try:
        demo_user = db.query(User).filter(User.username == "demo").first()
        if not demo_user:
            user = User(
                username="demo",
                hashed_password=get_password_hash("demo123"),
            )
            db.add(user)
            db.commit()
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
def read_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}
