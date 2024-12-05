from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField('Add')