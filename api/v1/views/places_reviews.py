#!/usr/bin/python3
"""Handles all default RESTFul API actions for reviews"""
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def list_all_reviews():
    """List all reviews"""
    pass


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_review(review_id):
    """Retrieve a review"""
    pass


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_review(review_id):
    """Delete a review"""
    pass


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_a_review():
    """Create a review"""
    pass


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_a_review(review_id):
    """Update a review"""
    pass
