from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


class EditForm(FlaskForm):
    rating = StringField(validators=[DataRequired()])
    edit = SubmitField('Change Rating')