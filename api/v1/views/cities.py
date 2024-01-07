#!/usr/bin/python3
"""Handles all default RESTFul API actions for cities"""
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def list_all_cities(state_id):
    """List all cities in a state"""
    pass


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_city(city_id):
    """Retrieve a city"""
    pass


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_city(city_id):
    """Delete a state"""
    pass


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_a_city(state_id):
    """Create a city in a state"""
    pass


@app_views.route('/cities/<city_id', methods=['PUT'], strict_slashes=False)
def update_a_city(city_id):
    """Update a city"""
    pass
