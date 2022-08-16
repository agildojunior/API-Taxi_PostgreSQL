import jwt
import datetime
from config import app
from flask import jsonify, request
from .entities import Empresas
from config import db

def get_all(current_empresa):
  rest = Empresas.query.all()
  return jsonify([empresas.to_json() for empresas in rest]), 200

def get_by_id(current_empresa,id):
  rest = Empresas.query.get(id)
  if rest is None:
    return "Nao encontrado", 404
  return jsonify(rest.to_json())

def insert(current_empresa):
  if request.is_json:
    body = request.get_json()
    res = Empresas (
      nome = body["nome"],
      cnpj = body["cnpj"]
    )
    db.session.add(res)
    db.session.commit()
    payload = {
    "cnpj": res.cnpj,
    "exp" : datetime.datetime.utcnow()
    } 
    token = jwt.encode(payload,app.config["SECRET_KEY"])
    return jsonify(res.to_json(),token) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(current_empresa,id):
  if request.is_json:
    body = request.get_json()
    rest = Empresas.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    if("nome" in body):
      rest.nome = body["nome"]
    if("cnpj" in body):
      rest.cnpj = body["cnpj"]
      
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415
