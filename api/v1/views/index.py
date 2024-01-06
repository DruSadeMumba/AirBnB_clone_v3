#!/usr/bin/python3
"""Index Blueprint"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    "Returning the status of the API upon the get request."
    return jsonify(status='OK')
