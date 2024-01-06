#!/usr/bin/python3
"""Index Blueprint"""
from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    """Returning the status of the API upon the get request."""
    return jsonify(status='OK')


@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stats():
    """Return the number of the instances in the class."""
    number_of_amenities = storage.count(Amenity)
    number_of_cities = storage.count(City)
    number_of_places = storage.count(Place)
    number_of_reviews = storage.count(Review)
    number_of_states = storage.count(State)
    number_of_users = storage.count(User)

    return {
        "amenities": number_of_amenities,
        "cities": number_of_cities,
        "places": number_of_places,
        "reviews": number_of_reviews,
        "states": number_of_states,
        "users": number_of_users,
    }
