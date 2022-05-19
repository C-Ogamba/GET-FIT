from app import db
from flask_login import current_user
from app import login
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    # img_file=db.Column(db.String(130))
    
   
    def set_password(self, password):
            self.password = generate_password_hash(password)
    def check_password(self, password):
            return check_password_hash(self.password, password)
    def __repr__(self):
        return f'User {self.username}'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classes=db.Column(db.String())
    package=db.Column(db.String())
    trainer=db.Column(db.String())


    def __repr__(self):
        return '<User {}>'.format(self.classes)
