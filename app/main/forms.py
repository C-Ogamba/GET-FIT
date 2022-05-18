from flask_wtf import FlaskForm
from wtforms import SubmitField,TextArea,StringField,SelectField
from wtforms.validators import Required

class AddActivity(FlaskForm):
    title = StringField("Class Title", validators = [DataRequired()])
    category = SelectField("What category are you submitting to?", choices=[("sportdances", "Sportdances"), ( "bodybuilding", "Bodybuilding")],validators=[DataRequired()])
    description = TextAreaField('Are you ready for fun in a healthy way' ,validators = [DataRequired()] )
    submit = SubmitField('Submit')
    
    class TrainerForm(FlaskForm):
        description = TextAreaField('Add a Trainer',validators =[DataRequired])
        submit = SubmitField('Submit')
        
    class PricesForm(FlaskForm):
        category = SelectField('Affordable prices',choices=[("basic","Basic"), ("unlimited","Unlimited")],validators=[DataRequired])
        description = TestAreaField('Are you ready to pay for our gym services',validators = [DataRequired]) 
        submit = SubmitField('Submit')
    
    