from flask import render_template, redirect, url_for, flash, request
from ..models import User
from .. import db
from . import auth
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required
from ..email import mail_message


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_pasword(form.pasword.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for ('main.index'))
        flash('Invalid username or pasword')
    return render_template('auth/login.html', loginform = form)        

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,pasword = form.pasword.data)
        user.save_u()

        mail_message("Welcome to Pitch","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html',registration_form = form)

