from flask import jsonify, request
from .entities import Empresas
from config import db

def get_all():
  rest = Empresas.query.all()
  return jsonify([empresas.to_json() for empresas in rest]), 200

def get_by_id(id):
  rest = Empresas.query.get(id)
  if rest is None:
    return "Nao encontrado", 404
  return jsonify(rest.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    res = Empresas (
      nome = body["nome"],
      cnpj = body["cnpj"]
    )
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(id):
  if request.is_json:
    body = request.get_json()
    rest = Empresas.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    if("nome" in body):
      rest.nome = body["nome"]
    if("cpnj" in body):
      rest.cnpj = body["cnpj"]
      
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415
