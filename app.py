from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path='', static_folder='.')


# CORS section

@app.after_request
def after_request_func(response):
    response.headers.add("Access-Control-Allow-Origin", "")
    response.headers.add('Access-Control-Allow-Headers', "")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

# end CORS section


# 404 handle


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Your requested url could not be found: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404
    return res

# 403 handler


@app.errorhandler(403)
def forbidden(error=None):
    message = {
        'status': 403,
        'message': 'Forbidden',
    }
    res = jsonify(message)
    res.status_code = 403
    return res

from routes import login
from routes import signup
from routes import auth_status
from routes import username_check
from routes import post_upload
from routes import post_getinfo


# Add your API endpoints here


# @app.route('/')
# def get_endpoint_function():
#     try:
#         res = "<h1 style='position: fixed; top: 50%;  left: 50%; transform: translate(-50%, -50%);'>FLASK API HOME</h1>"
#         return res

#     except Exception as e:
#         print(e)


if __name__ == "__main__":
    app.run()
