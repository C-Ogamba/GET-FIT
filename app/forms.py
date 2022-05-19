from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired

class AddActivity(FlaskForm):
    # title = StringField("Class Title", validators=[DataRequired()])
    category = SelectField("What category are you submitting to?", choices=[("sportdances", "Sportdances"), ( "bodybuilding", "Bodybuilding")],validators=[DataRequired()])
    description = TextAreaField('Are you ready for fun in a healthy way' ,validators = [DataRequired()] )
    submit = SubmitField('Submit')
    
class TrainerForm(FlaskForm):
    category = SelectField("Which trainer do you chose to?", choices=[("shivsimani", "Shivsimani"), ( "chikikiruka", "Chikikiruka,")],validators=[DataRequired()])
    description = TextAreaField('Add a Trainer',validators =[DataRequired()])
    submit = SubmitField('Submit')
            
class PricesForm(FlaskForm):
    category = SelectField('Affordable prices',choices=[("basic","Basic"), ("unlimited","Unlimited")],validators=[DataRequired()])
    description = TextAreaField('Are you ready to pay for our gym services',validators = [DataRequired()]) 
    submit = SubmitField('Submit')
        
    