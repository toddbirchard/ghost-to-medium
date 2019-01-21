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
        r.set('token', app.config['TOKEN'])
        r.set('clientid', app.config['CLIENT_ID'])
        r.set('clientsecret', app.config['CLIENT_SECRET'])
        r.set('publication', app.config['PUBLICATION'])
        r.set('endpoint_me', app.config['ME_ENDPOINT'])


        # Import our modules
        from . import main

        return app
