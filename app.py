from flask import Flask
from blueprints.static_pages import static_pages
from blueprints.dashboard import dashboard
from blueprints.profiles import profiles
from blueprints.settings import settings

app = Flask(__name__)

# Register blueprints with URL prefixes
app.register_blueprint(static_pages)
app.register_blueprint(dashboard)
app.register_blueprint(profiles, url_prefix='/user')
app.register_blueprint(settings, url_prefix='/settings')

if __name__ == '__main__':
    app.run(debug=True)
