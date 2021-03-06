import string
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField,PasswordField,BooleanField
from wtforms.validators import Email,DataRequired,EqualTo,Length,ValidationError
from app import LoginManager
from app.models import User



class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=4,max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'{username.data} is already taken. Please choose another username')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'{email.data} is already taken. Please choose another email')

class Login(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class productForm(FlaskForm):
    classes = SelectField("Pick the class pick", choices=[( 1,  "Sportdances"), ( 2, "Bodybuilding")],validators=[DataRequired()] )
    trainer = SelectField("Pick your preffered trainer", choices=[(1, "Shivsimani"), ( 2, "Chikikiruka,")],validators=[DataRequired()])
    package= SelectField('Select package',choices=[(200,"Basic"), (300,"Unlimited")],validators=[DataRequired()])
    submit = SubmitField('Submit')





 
  