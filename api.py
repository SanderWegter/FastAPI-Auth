from fastapi import FastAPI
from starlette.requests import Request

import os
from routes.v1 import auth, user
from time import time

app = FastAPI(
  title="FastAPI - Auth example",
  description="FastAPI - Auth example using JWT",
  version="0.0.1"
)

app.include_router(
  auth.router,
  prefix='/v1/auth',
  tags=["Authentication"]
)
app.include_router(
  user.router,
  prefix='/v1/user',
  tags=["User"]
)

#For testing - just run python3 api.py
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=6060)