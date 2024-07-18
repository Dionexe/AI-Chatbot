from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, logout_user
from forms import RegistrationForm, LoginForm
from models import User
from app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.chatbot'))

    reg_form = RegistrationForm()
    login_form = LoginForm()

    if reg_form.submit.data and reg_form.validate_on_submit():
        user = User(username=reg_form.username.data, email=reg_form.email.data)
        user.set_password(reg_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        login_user(user)
        return redirect(url_for('main.chatbot'))

    if login_form.submit.data and login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and user.check_password(login_form.password.data):
            flash('You have been logged in!', 'success')
            login_user(user)
            return redirect(url_for('main.chatbot'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('index.html', reg_form=reg_form, login_form=login_form)

@main.route('/chatbot')
@login_required
def chatbot():
    return render_template('chatbot.html', title='AI Chatbot')

@main.route('/logout', methods=['POST'])
@login_required  # Ensure the user is logged in before they can log out
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('main.home'))