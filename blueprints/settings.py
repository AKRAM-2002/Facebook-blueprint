from flask import Blueprint, render_template

settings = Blueprint('settings', __name__)

@settings.route('/settings')
def settings_home():
    return render_template('settings_home.html')

@settings.route('/settings/security')
def security():
    return render_template('security.html')

@settings.route('/settings/privacy')
def privacy():
    return render_template('privacy.html')
