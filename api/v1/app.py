#!/usr/bin/env python3
"""Entry point for the routing to return API Status."""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)

get_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
get_port = int(os.getenv("HBNB_API_PORT", 5000))

CORS(app, resources={'/*': {'origins': get_host}})

app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def resource_not_found(error):
    """Handling user request if not found."""
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def bad_request(error):
    """Handling the bad request."""
    message = error.get_description()
    return {"error": message}, 400


@app.teardown_appcontext
def close(session=None):
    """Close when session closed."""
    storage.close()


if __name__ == "__main__":
    app.run(host=get_host, port=(get_port), threaded=True)
