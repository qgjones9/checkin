from flask import jsonify

from app import app


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'errorcode': 500, 'message': 'check your json data'})


# error handlers
@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})
