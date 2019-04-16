from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from lib.Auth import Auth

router = APIRouter()
auth = Auth()

class Token(BaseModel):
  access_token: str
  token_type: str

@router.post(
  '/get_token',
  response_model=Token,
  response_description="Returns user access token",
  summary="Authenticate API user",
  description="Authenticate an API user and return a token for subsequent requests"
)
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
  a = auth.login(form_data.username, form_data.password)
  if a and a["status"] == "error":
    raise HTTPException(status_code=400, detail={"status": "error", "message": a["message"]})
  return {"access_token": a["token"], "token_type": "bearer"}