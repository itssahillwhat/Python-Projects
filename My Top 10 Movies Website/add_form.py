from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, FloatField


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    add = SubmitField('Add Movie')