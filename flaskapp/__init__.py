from flask import Flask
from .config import Config
from flask_restful import Api

def create_app(config_class=Config):
    app = Flask(__name__)
    api = Api()
    app.config.from_object(Config)

    # Initializing API routes
    from flaskapp.api.routes import initialise_api_routes
    initialise_api_routes(api)

    api.init_app(app)

    from flaskapp.api.routes import api_bp

    app.register_blueprint(api_bp)

    return app
