from sqlalchemy import Integer, String, Column, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base

class Like(Base) :
    __tablename__ = "likes"
    __table_args__ = (UniqueConstraint("post_id", "user_id"),) #table_args attend un tuple(liste figee) meme s'il n'ya qu'un seul element. en python (X) tout seul n'est pas un tuple c'est juste un x entre paranthese or (x,) est un tuple a un element la virgule est donc obligatoire
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    author = relationship("User")