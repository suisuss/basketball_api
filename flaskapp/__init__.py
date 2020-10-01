from flask import Flask
from .config import Config
from flask_restful import Api
from flask_minify import minify

app = Flask(__name__)
api = Api()


def create_app(app=app, config_class=Config, api=api):
    app.config.from_object(Config)

    # Initializing API routes
    from flaskapp.api.routes import initialise_api_routes
    initialise_api_routes(api)

    api.init_app(app)

    from flaskapp.api.routes import api_bp

    app.register_blueprint(api_bp)

    minify(app)

    return app


app = create_app()
