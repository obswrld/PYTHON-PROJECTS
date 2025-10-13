from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def sign_up():
    return "Sign Up Page"

@auth.route('/login')
def login():
    return "Login Page"

@auth.route('/logout')
def logout():
    return "Logout Page"