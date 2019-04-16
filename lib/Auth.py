from fastapi import HTTPException
from lib.Database import Database
from lib.Config import Config
import bcrypt
import jwt
from datetime import datetime, timedelta
import os

class Auth:
  def __init__(self):
    self.db = Database()
    self.config = Config().getConfig()
    self.key = self.config['server_settings']['app_key']
  
  def login(self, username, password):
    cur = self.db.query("""
      SELECT
        password,
        user_description
      FROM
        users
      WHERE
        username = %s
    """, [username])

    r = cur.fetchone()
    if not r:
      return {"status": "error", "mesage": "username/password incorrect"}
    
    db_password, user_description = r

    pwbytes = password.encode('utf-8')
    saltbytes = db_password.encode('utf-8')

    if bcrypt.hashpw(pwbytes, saltbytes) == saltbytes:
      token = jwt.encode({
        'sub': username,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(seconds=self.config['server_settings']['expiry']),
        'fln': user_description
      },
      self.key)

      return {"status": "success", "token": token.decode('utf-8')}
    return {"status": "error", "message": "username/password incorrect"}

  def validate(self, token):
    try:
      data = jwt.decode(token, self.key)
    except Exception as e:
      if "expired" in str(e):
        raise HTTPException(status_code=400, detail={"status": "error", "message": "Token expired"})
      else:
        raise HTTPException(status_code=400, detail={"status": "error", "message": "Exception: " + str(e)})
    return data