import string
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired


#activity form
class productForm(FlaskForm):
    classes = SelectField("Pick the class pick", choices=[("1", "Sportdances"), ( "2", "Bodybuilding")],validators=[DataRequired()] ,coerce=string)
    trainer = SelectField("Pick your preffered trainer", choices=[("trainer 1", "Shivsimani"), ( "trainner 2", "Chikikiruka,")],validators=[DataRequired()])
    package= SelectField('Select package',choices=[("package 1","Basic"), ("package 2","Unlimited")],validators=[DataRequired()])
    submit = SubmitField('Submit')



 
  