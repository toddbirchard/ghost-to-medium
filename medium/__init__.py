from flask import Flask
from flask_redis import FlaskRedis

# Set global entities
r = FlaskRedis()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Initiate globals
        r.init_app(app, charset="utf-8", decode_responses=True)

        # Set global contexts
        r.set('uri', app.config['SQLALCHEMY_DATABASE_URI'])
        r.set('baseurl',  app.config['BASE_URL'])

        # Import our modules
        from . import app

        return app
