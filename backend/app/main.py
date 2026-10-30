from fastapi import FastAPI
from app.routes import auth
from app.routes import users

app = FastAPI(
title="ITConnect API",
version="1.0.0",
)

app.include_router(auth.router)
app.include_router(users.router)
    
@app.get("/health")
def health_check():
    return {"status": "ok"}