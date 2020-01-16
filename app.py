#!flask/bin/python
import os
from flask import Flask, jsonify, abort, make_response, request
from joblib import load

BAD_REQUEST = 'Bad Request'
FORBIDDEN = 'Forbidden'
CONFLICT = 'Conflict'
UNAUTHORIZED = 'Unauthorized'
NOT_FOUND = 'Not Found'
UNPROCESSABLE_ENTITY = 'Unprocessessable Entity'
NOT_ALLOWED = 'Not Allowed'

app = Flask(__name__)

def _predict_clf(input):
    input = [input]
    clf = load('model.joblib')
    return clf.predict(input)

@app.route('/api/load', methods=['POST'])
def create_item():
    if not request.json or 'input' not in request.json:
        abort(400)

    input = request.json.get('input')
    if type(input) is not str:
        abort(422)

    pred = _predict_clf(input)

    return jsonify({'output': pred[0]}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)

@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'error': FORBIDDEN}), 403)

@app.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': CONFLICT}), 409)

@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': UNAUTHORIZED}), 401)
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)

@app.errorhandler(422)
def unpreocessable_entity(error):
    return make_response(jsonify({'error': UNPROCESSABLE_ENTITY}), 422)

@app.errorhandler(405)
def not_allowed(error):
    return make_response(jsonify({'error': NOT_ALLOWED}), 405)

if __name__ == '__main__':
    app.run()