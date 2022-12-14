from flask import jsonify, request
from .entities import Taxis
from config import db

def get_all(current_empresa):
  rest = Taxis.query.all()
  return jsonify([taxis.to_json() for taxis in rest]), 200

def get_by_id(current_empresa,id):
  rest = Taxis.query.get(id)
  if rest is None:
    return "Nao encontrado", 404
  return jsonify(rest.to_json())

def insert(current_empresa):
  if request.is_json:
    body = request.get_json()
    res = Taxis (
        telefone_taxista = body["telefone_taxista"],
        id_usuario = body["id_usuario"],
        modelo_taxi = body["modelo_taxi"],
        placa_taxi = body["placa_taxi"]
    )
    db.session.add(res)
    db.session.commit()
    
    return jsonify(res.to_json()) , 201

  return {"error": "Os dados devem ser JSON"}, 415

def update(current_empresa,id):
  if request.is_json:
    body = request.get_json()
    rest = Taxis.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    if("telefone_taxista" in body):
      rest.telefone_taxista = body["telefone_taxista"]
    if("id_usuario" in body):
      rest.id_usuario = body["id_usuario"]
    if("modelo_taxi" in body):
      rest.modelo_taxi = body["modelo_taxi"]
    if("placa_taxi" in body):
      rest.placa_taxi = body["placa_taxi"]
      
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415

def delete(current_empresa,id):
  rest = Taxis.query.get(id)
  if rest is None:
      return {"error": {"error": "Nao encontrado"}}, 404
  rest.ativo = False
  db.session.add(rest)
  db.session.commit()
  return {"message": "Deletado com sucesso"}, 200