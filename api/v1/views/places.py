#!/usr/bin/python3
"""Handles all default RESTFul API actions for places"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def list_all_places(city_id):
    """List all places"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def retrieve_a_place(place_id):
    """Retrieve a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_a_place(place_id):
    """Delete a place"""
    place = storage.get(Place, place_id)
    if place:
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_a_place(city_id):
    """Create a place"""
    city = storage.get(City, city_id)
    data = request.get_json()
    if not city:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    new = Place(**data)
    new.city_id = city_id
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_a_place(place_id):
    """Update a place"""
    place = storage.get(Place, place_id)
    data = request.get_json()
    if not place:
        abort(404)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, val in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, val)
    storage.save()
    return jsonify(place.to_dict()), 200


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search():
    """Retrieves all places depending on the JSON in the body of the request"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    states = data.get('states', [])
    cities = data.get('cities', [])
    amenities = data.get('amenities', [])

    if not (states or cities or amenities):
        return jsonify([place.to_dict().pop('amenities', None)
                        for place in storage.all(Place).values()])
    places = []
    if states:
        state = [storage.get(State, state_id) for state_id in states]
        places.extend(place for state in map(lambda x: x if x else None, state)
                      for city in state.cities if state and city
                      for place in city.places)
    if cities:
        city = [storage.get(City, city_id) for city_id in cities]
        places.extend(place for city in city if city for place in city.places
                      if place not in places)
    if amenities:
        if not places:
            places = [place for place in storage.all(Place).values()]
        amenity = [storage.get(Amenity, amenity_id)
                   for amenity_id in amenities]
        places = [place for place in places if all(amen in place.amenities
                                                   for amen in amenity)]
    return jsonify([place.to_dict().pop('amenities', None)
                    for place in places])