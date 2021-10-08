from flask import Blueprint, render_template, redirect, url_for


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    pass


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    pass


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
