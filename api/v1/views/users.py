#!/usr/bin/python3
"""Handles all default RESTFul API actions for users"""
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_all_users():
    """List all users"""
    pass


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_user(user_id):
    """Retrieve a user"""
    pass


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_user(user_id):
    """Delete a user"""
    pass


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_a_user():
    """Create a user"""
    pass


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_a_user(user_id):
    """Update a user"""
    pass
