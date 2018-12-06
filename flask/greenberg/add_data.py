from app import db
from app.models import User, Post

u = User(username='inbar', email='inbar@eisenberg.com')
db.session.add(u)
db.session.commit()

db.session.add(User(username='rachel', email='rachel@eisenberg.com'))
db.session.commit()

users=User.query.all()
for u in users:
    print(u.id,u.username)

