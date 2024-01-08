#!/usr/bin/python3
"""Entry point for the routing to return API Status."""
import os
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(arg=None):
    """Close session when app content torn down."""
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """404 page"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    get_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    get_port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=get_host, port=get_port, threaded=True)
