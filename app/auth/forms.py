from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('REmember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), Email(), EqualTo('password_confirm', message = 'Password must match')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("The email has already been taken!")

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("The username has already been take!")     