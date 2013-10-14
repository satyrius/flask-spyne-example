from flask import Flask
from api.views import api


def create_app():
    app = Flask(__name__)

    # Register flask app submodules
    app.register_blueprint(api, url_prefix='/api')

    return app
