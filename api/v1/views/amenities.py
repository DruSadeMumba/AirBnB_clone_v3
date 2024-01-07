#!/usr/bin/python3
"""Handles all default RESTFul API actions for amenities"""
from flask import abort, jsonify, request

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def list_all_amenities():
    """List all amenities"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_amenity(amenity_id):
    """Retrieve an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    return jsonify(amenity.to_dict() if amenity else abort(404))


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_a_amenity(amenity_id):
    """Delete an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_a_amenity():
    """Create an amenity"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new = Amenity(**data)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_a_amenity(amenity_id):
    """Update an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    data = request.get_json()
    if not amenity:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, val in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, val)
    storage.save()
    return jsonify(amenity.to_dict()), 200
