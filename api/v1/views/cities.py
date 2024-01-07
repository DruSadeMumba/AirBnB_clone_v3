#!/usr/bin/python3
"""Handles all default RESTFul API actions for cities"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def list_all_cities(state_id):
    """List all cities in a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_city(city_id):
    """Retrieve a city"""
    city = storage.get(City, city_id)
    return jsonify([city.to_dict() if city else abort(404)])


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_city(city_id):
    """Delete a state"""
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_a_city(state_id):
    """Create a city in a state"""
    state = storage.get(State, state_id)
    data = request.get_json()
    if not state:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new = City(**data)
    new.state_id = state_id
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_a_city(city_id):
    """Update a city"""
    city = storage.get(City, city_id)
    data = request.get_json()
    if not city:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, val in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, val)
    storage.save()
    return jsonify(city.to_dict()), 200
