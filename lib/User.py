from lib.Database import Database

class User:
  def __init__(self):
    self.db = Database()

  def get_users(self):
    cur = self.db.query("""
      SELECT
        username,
        user_description
      FROM
        users
    """)

    users = []
    for u in cur.fetchall():
      username, description = u
      users.append({
        "username": username,
        "description": description
      })
    
    return {"users": users}