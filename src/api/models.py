from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from enum import Enum

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Address(db.Model):
    __tablename__='address'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    directions = db.Column(db.String(120), unique=False, nullable=False)
    district = db.Column(db.String(120), unique=False, nullable=False)
    province = db.Column(db.String(120), unique=False, nullable=False)
    state = db.Column(db.String(120), unique=False, nullable=False)
    googlemapslink = db.Column(db.String(300), unique=False, nullable=True)

    def __repr__(self):
        return f'<Address {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "directions": self.directions,
            "district": self.district,
            "province": self.province,
            "state": self.state,
            "googlemapslink": self.googlemapslink     
        }

class Lessons(db.Model):
    __tablename__='lessons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False, nullable=False)
    price = db.Column(db.String(25), unique = False, nullable = True)


    def __repr__(self):
        return f'<Lessons {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price  
        }

class Reviews(db.Model):
    __tablename__='reviews'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    review = db.Column(db.String(400), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique = False, nullable=False)

    def __repr__(self):
        return f'<Reviews {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "review": self.review,
            "rating": self.rating  
        }