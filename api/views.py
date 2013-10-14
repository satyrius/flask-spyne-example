import json
from flask import Blueprint, make_response, current_app


api = Blueprint('api', __name__)


@api.route('/version')
def version():
    response = make_response(json.dumps({
        'version': 'demo',
        'hello': current_app.config['HELLO'],
    }))
    response.headers['Content-Type'] = 'application/json'
    return response
