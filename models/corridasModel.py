from flask import jsonify, request
from .entities import Corridas
from config import db

def get_all(current_empresa):
  rest = Corridas.query.all()
  return jsonify([corridas.to_json() for corridas in rest]), 200

def get_by_id(current_empresa,id):
  rest = Corridas.query.get(id)
  if rest is None:
    return "Nao encontrado", 404
  return jsonify(rest.to_json())

def insert(current_empresa):
  if request.is_json:
    body = request.get_json()
    res = Corridas (
      # origem = body['origem'],
      # destino = body['destino'],
      # nome_usuario = None,
      # id_empresa = None,
      # id_taxi = None,
    )
    if("origem" in body):
      res.origem = body["origem"]
    if("destino" in body):
      res.destino = body["destino"]
    if("status" in body):
      res.status = body["status"]
    if("nome_usuario" in body):
      res.nome_usuario = body["nome_usuario"]
    if("id_empresa" in body):
      res.id_empresa = body["id_empresa"]
    if("id_taxi" in body):
      res.id_taxi = body["id_taxi"]
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(current_empresa,id):
  if request.is_json:
    body = request.get_json()
    rest = Corridas.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    if("origem" in body):
      rest.origem = body["origem"]
    if("destino" in body):
      rest.destino = body["destino"]
    if("status" in body):
      rest.status = body["status"]
    if("nome_usuario" in body):
      rest.nome_usuario = body["nome_usuario"]
    if("id_empresa" in body):
      rest.id_empresa = body["id_empresa"]
    if("id_taxi" in body):
      rest.id_taxi = body["id_taxi"]
    
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415

def delete(current_empresa,id):
  rest = Corridas.query.get(id)
  if rest is None:
      return {"error": {"error": "Nao encontrado"}}, 404
  rest.ativo = False
  db.session.add(rest)
  db.session.commit()
  return {"message": "Deletado com sucesso"}, 200