#!/usr/bin/python3
"""Entry point for the routing to return API Status."""
import os
from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(arg=None):
    """Close session when app content torn down."""
    storage.close()


if __name__ == "__main__":
    get_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    get_port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=get_host, port=get_port, threaded=True)
