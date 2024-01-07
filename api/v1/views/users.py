#!/usr/bin/python3
"""Handles all default RESTFul API actions for users"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_all_users():
    """List all users"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_user(user_id):
    """Retrieve a user"""
    user = storage.get(User, user_id)
    return jsonify(user.to_dict() if user else abort(404))


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_user(user_id):
    """Delete a user"""
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_a_user():
    """Create a user"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'email' not in data:
        return jsonify({"error": "Missing email"}), 400
    if 'password' not in data:
        return jsonify({"error": "Missing password"}), 400
    new = User(**data)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_a_user(user_id):
    """Update a user"""
    user = storage.get(User, user_id)
    data = request.get_json()
    if not user:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, val in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, val)
    storage.save()
    return jsonify(user.to_dict()), 200
