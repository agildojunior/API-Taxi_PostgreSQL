from flask import jsonify, request
from models import Taxis
from config import db

def get_all():
    return Taxis.get_all()

def get_by_id(id):
    return Taxis.get_by_id(id)

def insert():
    return Taxis.insert()

def update(id):
    return Taxis.update(id)