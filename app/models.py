from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash


class AddActivity(db.Model):
    __tablename__ = 'activity'
    category = db.Column(db.String(255), index = True,nullable = False)
    description = db.Column(db.Text)
    
    
    @classmethod
    def get_activity(cls, id):
        activity = AddActivity.query.order_by(actity_id=id).desc().all()
        return activity

    def __repr__(self):
        return f'Addactivety {self.description}'   
   
class TrainerForm(db.Model):
    __tablename__ = 'trainer'
    category = db.Column(db.String(255), index = True,nullable = False)
    description = db.Column(db.Text)
    
    
    @classmethod
    def get_trainer(cls, id):
        trainer = TrainerForm.query.order_by(trainer_id=id).desc().all()
        return trainer

    def __repr__(self):
        return f'trainer {self.description}'   
    
    class PriceForm(db.Model):
        __tablename__ = 'prices'
        category = db.Column(db.String(255), index = True,nullable = False)
        description = db.Column(db.Text)
    
    
    @classmethod
    def get_prices(cls, id):
        trainer = PriceForm.query.order_by(price_id=id).desc().all()
        return prices

    def __repr__(self):
        return f'price {self.description}'   