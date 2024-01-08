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
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    if data and len(data):
        states = data.get('states', None)
        cities = data.get('cities', None)
        amenities = data.get('amenities', None)

    if not data or not any([states, cities, amenities]):
        return jsonify([place.to_dict() for place in
                        storage.all(Place).values()])

    list_places = []
    if states:
        state = [storage.get(State, state_id) for state_id in states]
        list_places.extend(place for state in state if state
                           for city in state.cities if city
                           for place in city.list_places)

    if cities:
        city = [storage.get(City, city_id) for city_id in cities]
        for cty in city:
            if cty:
                for place in cty.list_places:
                    if place not in list_places:
                        list_places.append(place)

    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [place for place in list_places
                       if all([am in place.amenities
                               for am in amenities_obj])]

    places = []
    for plac in list_places:
        d = plac.to_dict()
        d.pop('amenities', None)
        places.append(d)

    return jsonify(places)
