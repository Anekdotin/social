__author__ = 'ed'
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo, form
from models import User




def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("Username exists")

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError("email exists")

class RegistrationForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message="Username should be one word, letters and numbers only"
            ),
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists


        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=5),
            EqualTo('password2', message='Passwords dont match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=([DataRequired()]
        )

    )

