#!/usr/bin/python3
"""Handles all default RESTFul API actions for places"""
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def list_all_places():
    """List all places"""
    pass


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_place(place_id):
    """Retrieve a place"""
    pass


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_place(place_id):
    """Delete a place"""
    pass


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_a_place():
    """Create a place"""
    pass


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_a_place(place_id):
    """Update a place"""
    pass
