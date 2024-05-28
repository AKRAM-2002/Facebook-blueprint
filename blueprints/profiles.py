from flask import Blueprint, render_template

profiles = Blueprint('profiles', __name__)

@profiles.route('/user/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@profiles.route('/user/<username>/photos')
def photos(username):
    return render_template('photos.html', username=username)
