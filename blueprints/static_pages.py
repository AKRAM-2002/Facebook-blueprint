from flask import Blueprint, render_template

static_pages = Blueprint('static_pages', __name__)

@static_pages.route('/')
def home():
    return render_template('home.html')

@static_pages.route('/register')
def register():
    return render_template('register.html')

@static_pages.route('/about')
def about():
    return render_template('about.html')
