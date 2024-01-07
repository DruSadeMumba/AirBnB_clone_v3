#!/usr/bin/python3
"""Handles all default RESTFul API actions for reviews"""
from flask import abort, jsonify, request

from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def list_all_reviews(place_id):
    """List all reviews"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify([review.to_dict() for review in place.reviews])


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_review(review_id):
    """Retrieve a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_a_review(review_id):
    """Delete a review"""
    review = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_a_review(place_id):
    """Create a review"""
    place = storage.get(Place, place_id)
    data = request.get_json()
    if not place:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if 'text' not in data:
        return jsonify({"error": "Missing text"}), 400
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    new = Review(**data)
    new.place_id = place_id
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_a_review(review_id):
    """Update a review"""
    review = storage.get(Review,  review_id)
    data = request.get_json()
    if not review:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for k, val in data.items():
        if k not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, k, val)
    storage.save()
    return jsonify(review.to_dict()), 200
