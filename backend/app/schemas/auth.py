from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="Adresse email de l'utilisateur")
    password: str = Field(...,min_length=8, description="Mot de passe de l'utilisateur")

class TokenResponse(BaseModel):
    access_token: str = Field(..., description="Jeton d'accès pour l'authentification")
    token_type: str = Field(..., description="Type de jeton (ex: 'bearer')")