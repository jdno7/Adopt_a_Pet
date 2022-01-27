from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):

    name = StringField('Pet Name')
    species = StringField('Species', validators=[AnyOf(['Dog','Cat','Porcupine'], message='must be Dog Cat or Porcupine')])
    photo_url = StringField('Photo', validators=[URL(message="Must be a valide Photo URL")])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30,message="Shit it too Old")])
    notes = StringField('Notes')

class EditPetForm(FlaskForm):
 
    photo_url = StringField('Photo', validators=[URL(message="Must be a valide Photo URL")])
    notes = StringField('Notes')
    available = SelectField('Availability', choices=[(True,'Available'),(False, 'Unavailable' )], coerce=bool)