from app.schemas.common import OrmBaseModel

class TokenResponse(OrmBaseModel):
    access_token:str
    refresh_token:str
    token_type:str

