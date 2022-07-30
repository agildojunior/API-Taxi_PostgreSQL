from flask import jsonify, request
from models import Corridas
from config import db

def get_all():
    return Corridas.get_all

def get_by_id(id):
    return Corridas.get_by_id

def insert():
    return Corridas.insert

def update(id):
    return Corridas.update
