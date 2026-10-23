from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class RegisterRequest (BaseModel):
    email: EmailStr = Field(..., description="Adresse email de l'utilisateur")
    password: str = Field(min_length=8, description="Mot de passe (minimum 8 caracteres)")

class UserResponse (BaseModel):
    id: int = Field(..., description="Identifiant Unique de l'utilisateur")
    email: EmailStr = Field(..., description="Adresse Email de l'utilisateur")
    created_at: datetime = Field(..., description="Date de creation du compte")