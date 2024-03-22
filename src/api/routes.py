"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Address, Reviews, Lessons, LessonsAddresses
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route("/admin_login", methods=["POST"])
def admin_login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
   
    if user is None:
        return jsonify({"msg": "User is not registered"}), 401

    if password != user.password :
        return jsonify({"msg": "Wrong password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route("/admin_signup", methods=["POST"])
def admin_signup():
    body = request.get_json()
    user = User.query.filter_by(email=body["email"]).first()

    if user == None:
        user = User(name=body["name"], email=body["email"], password=body["password"], is_active=True)

        db.session.add(user)
        db.session.commit()
        user_info = user.serialize()
        access_token = create_access_token(identity=user_info["id"])
        user_info['access_token']=access_token

        return jsonify(user_info), 200
    else:
        return jsonify({"msg": "user already exists with this email address"}), 401


@api.route('/get_addresses', methods=['GET'])
def get_addresses():
    all_addresses = Address.query.all()
    result = list(map(lambda item: item.serialize(), all_addresses))

    return jsonify(result) 

@api.route('/get_address/<int:address_id>', methods=['GET'])
def get_address(address_id):
    get_address = Address.query.filter_by(id=address_id).first()

    return jsonify(get_address.serialize())

@api.route('/add_address', methods=['POST'])
@jwt_required()
def add_address():

    body = request.get_json()
    address = Address(
        name = body['name'],
        directions = body['directions'],
        district = body['district'],
        province = body['province'],
        state = body['state'],
        googlemapslink = body['googlemapslink']
    )
    db.session.add(address)
    db.session.commit()

    response_body = {
        "message": "Address created"
    }

    return jsonify(response_body), 200

@api.route('/update_address/<int:address_id>', methods =['PUT'])
@jwt_required()
def update_address(address_id):
    body = request.get_json()
    update_address = Address.query.filter_by(id=address_id).first()
    print(update_address)
    print(body)
    if body['name']: update_address.name = body['name']
    if body['directions']: update_address.directions = body['directions']
    if body['district']: update_address.district = body['district']
    if body['province']: update_address.province = body['province']
    if body['state']: update_address.state = body['state']
    if body['googlemapslink']: update_address.state = body['googlemapslink']


    db.session.commit()

    response_body = {
        "message": "Address updated"
    }
      
    return jsonify(response_body), 200

@api.route('/delete_address/<int:address_id>', methods =['DELETE'])
def delete_address(address_id):
    delete_address = Address.query.filter_by(id=address_id).first()

    db.session.delete(delete_address)
    db.session.commit()

    response_body = {
        "message": "Address deleted"
    }
      
    return jsonify(response_body), 200

@api.route('/get_lessons', methods=['GET'])
def get_lessons():
    all_lessons = Lessons.query.all()
    result = list(map(lambda item: item.serialize(), all_lessons))

    return jsonify(result) 

@api.route('/get_lesson/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    get_lesson = Lessons.query.filter_by(id=lesson_id).first()

    return jsonify(get_lesson.serialize())

@api.route('/get_lesson_details/<int:lesson_id>/<int:address_id>', methods=['GET'])
def get_lesson_details(lesson_id, address_id):
    get_lesson_ids = LessonsAddresses.query.filter_by(lesson_id=lesson_id, address_id=address_id).first()
    print(get_lesson_ids)
    get_lesson_details = Lessons.query.filter_by(id=lesson_id).first()
    print(get_lesson_details.serialize())
    get_address_details = Address.query.filter_by(id=address_id).first()
    print(get_address_details.serialize())
    all_details = []
    all_details.append(get_address_details.serialize())
    all_details.append(get_lesson_details.serialize())
    all_details.append(get_lesson_ids.serialize())

    print(all_details)

    return jsonify(all_details)

@api.route('/add_lesson', methods=['POST'])
@jwt_required()
def add_lesson():

    body = request.get_json()
    lesson = Lessons(
        name = body['name'],
        description = body['description'],
        price = body['price']
    )
    db.session.add(lesson)
    db.session.commit()

    response_body = {
        "message": "Lesson created"
    }

    return jsonify(response_body), 200

@api.route('/update_lesson/<int:lesson_id>', methods =['PUT'])
@jwt_required()
def update_lesson(lesson_id):
    body = request.get_json()
    update_lesson = Lessons.query.filter_by(id=lesson_id).first()
    print(update_lesson)
    print(body)
    if body['name']: update_lesson.name = body['name']
    if body['description']: update_lesson.description = body['description']
    if body['price']: update_lesson.price = body['price']

    db.session.commit()

    response_body = {
        "message": "Lesson updated"
    }
      
    return jsonify(response_body), 200

@api.route('/delete_lesson/<int:lesson_id>', methods =['DELETE'])
def delete_lesson(lesson_id):
    delete_lesson = Lessons.query.filter_by(id=lesson_id).first()

    db.session.delete(delete_lesson)
    db.session.commit()

    response_body = {
        "message": "Lesson deleted"
    }
      
    return jsonify(response_body), 200

@api.route('/add_lesson_details/<int:lesson_id>/<int:address_id>', methods=['POST'])
@jwt_required()
def add_lesson_details(lesson_id, address_id):

    body = request.get_json()
    lesson_details = LessonsAddresses(
        lesson_id = lesson_id,
        address_id = address_id,
        date = body['date']
    )
    db.session.add(lesson_details)
    db.session.commit()

    response_body = {
        "message": "Lesson created"
    }

    return jsonify(response_body), 200


@api.route('/get_reviews', methods=['GET'])
def get_reviews():
    all_reviews = Reviews.query.all()
    result = list(map(lambda item: item.serialize(), all_reviews))

    return jsonify(result) 

@api.route('/get_review/<int:review_id>', methods=['GET'])
def get_review(review_id):
    get_review = Reviews.query.filter_by(id=review_id).first()

    return jsonify(get_review.serialize())

@api.route('/add_review', methods=['POST'])
@jwt_required()
def add_review():

    body = request.get_json()
    review = Reviews(
        name = body['name'],
        review = body['review'],
        rating = body['rating']
    )
    db.session.add(review)
    db.session.commit()

    response_body = {
        "message": "Review created"
    }

    return jsonify(response_body), 200

@api.route('/update_review/<int:review_id>', methods =['PUT'])
@jwt_required()
def update_review(review_id):
    body = request.get_json()
    update_review = Reviews.query.filter_by(id=review_id).first()
    print(update_review)
    print(body)
    if body['name']: update_review.name = body['name']
    if body['review']: update_review.review = body['review']
    if body['rating']: update_review.rating = body['rating']

    db.session.commit()

    response_body = {
        "message": "Review updated"
    }
      
    return jsonify(response_body), 200

@api.route('/delete_review/<int:review_id>', methods =['DELETE'])
def delete_review(review_id):
    delete_review = Reviews.query.filter_by(id=review_id).first()

    db.session.delete(delete_review)
    db.session.commit()

    response_body = {
        "message": "Review deleted"
    }
      
    return jsonify(response_body), 200