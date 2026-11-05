from fastapi import FastAPI
from app.routes import auth
from app.routes import users
from app.routes import posts
from app.routes import likes

app = FastAPI(
title="ITConnect API",
version="1.0.0",
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(likes.router)
    
@app.get("/health")
def health_check():
    return {"status": "ok"}