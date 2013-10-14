import json
from flask import Blueprint, make_response


api = Blueprint('api', __name__)


@api.route('/version')
def version():
    response = make_response(json.dumps({'version': 'demo'}))
    response.headers['Content-Type'] = 'application/json'
    return response
