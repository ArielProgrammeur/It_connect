from pydantic import BaseModel, Field, ConfigDict   
from datetime import datetime

class CommentRequest(BaseModel):
    content: str = Field(..., min_length=1, max_length=500, description="Contenu du commentaire")

class CommentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="Identifiant Unique du commentaire")
    author_id: int = Field(..., description="Identifiant de l'auteur du commentaire")
    post_id: int = Field(..., description="Identifiant du post commenté")
    content: str = Field(..., description="Contenu du commentaire")
    created_at: datetime = Field(..., description="Date de création du commentaire")
    

