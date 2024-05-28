from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def dashboard_view():
    return render_template('dashboard.html')

@dashboard.route('/dashboard/messages')
def messages():
    return render_template('messages.html')
