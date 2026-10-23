from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models import User
from app.core.security import hash_password
from app.schemas.user import RegisterRequest, UserResponse
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)) :
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user is not None:
        raise HTTPException(status_code=409, detail="Cette adresse email est deja utilisee")

    new_user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user 