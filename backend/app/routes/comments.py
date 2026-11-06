from app.models import User, Post, Comment
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.comment import CommentRequest, CommentResponse
from app.core.database import get_db
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/posts", tags=["comments"])

@router.post("/{post_id}/comments", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment(post_id: int, payload: CommentRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Introuvable")
    new_comment = Comment(content=payload.content, author_id=current_user.id, post_id=post_id)
    db.add(new_comment)   
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/{post_id}/comments", response_model=list[CommentResponse])
def list_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Introuvable")
    return db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.created_at.desc()).all()
