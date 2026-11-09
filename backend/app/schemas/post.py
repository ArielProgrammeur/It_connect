from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime



class PostRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Titre du post")
    content: str = Field(..., min_length=1, max_length=1000, description="Contenu du post")

class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="Identifiant Unique du post")
    title: str = Field(..., min_length=1, max_length=255, description="Titre du post")
    content: str = Field(..., min_length=1, max_length=1000, description="Contenu du post")
    author_id: int = Field(..., description="Auteur du post")
    created_at: datetime = Field(..., description="Date de creation du post")   