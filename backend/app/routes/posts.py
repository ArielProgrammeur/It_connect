from fastapi import APIRouter, Depends, HTTPException, status   
from sqlalchemy.orm import Session
from app.models import Post, User 
from app.schemas.post import PostResponse, PostRequest
from app.core.database import get_db
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Introuvable")
    return post

@router.post("", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def  created_post(payload: PostRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_post = Post(title=payload.title, content=payload.content, author_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("", response_model=list[PostResponse])
def list_posts(db: Session = Depends(get_db)):
  return db.query(Post).order_by(Post.created_at.desc()).all()
    