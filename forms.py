from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo