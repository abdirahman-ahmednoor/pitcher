from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    pasword = PasswordField('pasword', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    pasword = PasswordField('pasword', validators=[Required(), EqualTo('pasword_confirm',message = 'paswords must match')])
    pasword_confirm = PasswordField('Confirm pasword', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("The email has already been taken!")

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("The username has already been take!")     