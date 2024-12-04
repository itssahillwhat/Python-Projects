from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, FloatField


class EditForm(FlaskForm):
    rating = FloatField('Your Rating out 10, e.g:7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    edit = SubmitField('Done')