from app.models import Like, User, Post
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session  
from app.core.database import get_db
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/posts", tags=["likes"])

@router.post("/{post_id}/likes", status_code=status.HTTP_201_CREATED)
def like_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Introuvable")

    existing_like = db.query(Like).filter(Like.post_id == post_id, Like.user_id == current_user.id).first()
    if existing_like is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Vous avez deja like ce post")

    new_like = Like(post_id=post_id, user_id=current_user.id)
    db.add(new_like)
    db.commit()

@router.delete("/{post_id}/likes", status_code=status.HTTP_204_NO_CONTENT)
def unlike_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Introuvable")

    existing_like = db.query(Like).filter(Like.post_id == post_id, Like.user_id == current_user.id).first()
    if existing_like is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post ou Like Introuvable")
    db.delete(existing_like)
    db.commit()