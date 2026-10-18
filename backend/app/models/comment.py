from sqlalchemy import Integer, String, ForeignKey, Column, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.models.base import Base

class Comment(Base) :
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    author = relationship("User")
