from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.', validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices= [('Technology', 'Technology'), ('Business', 'Business'), ('Programming', 'Programming'),('Social', 'Social'), ('Religion', 'Religion'), ('Sports', 'Sports')], validators=[Required()])
    post = TextAreaField('Your pitch', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Comment')