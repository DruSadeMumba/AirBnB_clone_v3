#!/usr/bin/python3
"""Handles all default RESTFul API actions for amenities"""
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def list_all_amenities():
    """List all amenities"""
    pass


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_amenity(amenity_id):
    """Retrieve an amenity"""
    pass


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_amenity(amenity_id):
    """Delete an amenity"""
    pass


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_a_amenity():
    """Create an amenity"""
    pass


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_a_amenity(amenity_id):
    """Update an amenity"""
    pass
