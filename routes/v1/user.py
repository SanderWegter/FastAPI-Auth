from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from lib.Auth import Auth
from lib.User import User
from typing import List

router = APIRouter()
auth = Auth()
user = User()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/v1/auth/get_token')

class UserInfo(BaseModel):
  username: str
  description: str

class Users(BaseModel):
  users: List[UserInfo]

async def is_auth(token: str = Security(oauth2_scheme)):
  return auth.validate(token)

@router.get(
  '/',
  response_model=Users,
  response_description="Returns list of users",
  summary="Return a list of users",
  description="Return a list of users"
  )
async def get_users(*, token: str = Security(is_auth)):
  return user.get_users()