#!/usr/bin/python3
"""Handles all default RESTFul API actions for states"""
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_all_states():
    """List all states"""
    pass


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_state(state_id):
    """Retrieve a state"""
    pass


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_state(state_id):
    """Delete a state"""
    pass


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_a_state():
    """Create a state"""
    pass


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_a_state(state_id):
    """Update a state"""
    pass
