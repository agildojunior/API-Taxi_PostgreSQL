from flask import jsonify, request
from models import Empresas
from config import db

def get_all():
    return Empresas.get_all()

def get_by_id(id):
    return Empresas.get_by_id(id)

def insert():
    return Empresas.insert()

def update(id):
    return Empresas.update(id)
