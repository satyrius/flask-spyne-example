from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from api.views import api
from enterprise.views import wsgi_application as enterprise


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.default')

    # Register flask app submodules
    app.register_blueprint(api, url_prefix='/api')

    # SOAP services are distinct wsgi applications, we should use dispatcher
    # middleware to bring all aps together
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/enterprise': enterprise
    })

    return app
