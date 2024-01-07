#!/usr/bin/python3
"""Handles all default RESTFul API actions for states"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


def get_state(state_id):
    """get a state by id"""
    state = storage.get(State, state_id)
    return state if state else abort(404)


def json_err(msg, stat_code):
    """get json err"""
    return jsonify({msg}), stat_code


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_all_states():
    """List all states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_state(state_id):
    """Retrieve a state"""
    return jsonify(get_state(state_id).to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_a_state(state_id):
    """Delete a state"""
    state = get_state(state_id)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_a_state():
    """Create a state"""
    data = request.get_json()
    if not data:
        return json_err("Not a JSON", 400)
    if 'name' not in data:
        return json_err("Missing name", 400)
    new = State(**data)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_a_state(state_id):
    """Update a state"""
    state = get_state(state_id)
    data = request.get_json()
    if not data:
        return json_err("Not a JSON", 400)
    for key, val in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, val)
    storage.save()
    return jsonify(state.to_dict()), 200
