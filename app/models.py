from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    # img_file=db.Column(db.String(130))
   

    def __repr__(self):
        return '<User {}>'.format(self.username)


class User_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classes=db.Column(db.String())
    package=db.Column(db.String())
    trainer=db.Column(db.String())


    def __repr__(self):
        return '<User {}>'.format(self.classes)
