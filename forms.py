from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import InputRequired, EqualTo, Email, Length, Regexp, ValidationError