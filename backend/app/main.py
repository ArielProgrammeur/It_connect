from fastapi import FastAPI
from app.routes import auth

app = FastAPI(
title="ITConnect API",
version="1.0.0",
)

app.include_router(auth.router)
    
@app.get("/health")
def health_check():
    return {"status": "ok"}