from flask import jsonify, request
from .entities import Usuarios
from config import db

def get_all(current_empresa):
  rest = Usuarios.query.all()
  return jsonify([usuarios.to_json() for usuarios in rest]), 200

def get_by_id(current_empresa,id):
  rest = Usuarios.query.get(id)
  if rest is None:
    return "Não encontrado", 404
  return jsonify(rest.to_json())

def insert(current_empresa):
  if request.is_json:
    body = request.get_json()
    res = Usuarios (
        # nome_usuario = body['nome_usuario'],
        # email_usuario = body["email_usuario"],
        # senha_usuario = body["senha_usuario"],
        # id_taxis = body["id_taxis"]
    )
    if("nome_usuario" in body):
      res.nome_usuario = body["nome_usuario"]
    if("email_usuario" in body):
      res.email_usuario = body["email_usuario"]
    if("senha_usuario" in body):
      res.senha_usuario = body["senha_usuario"]
    if("id_taxis" in body):
      res.id_taxis = body["id_taxis"]
    if("tipo_usuario" in body):
      res.tipo_usuario = body["tipo_usuario"]
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(current_empresa,id):
  if request.is_json:
    body = request.get_json()
    rest = Usuarios.query.get(id)
    if rest is None:
      return "Não encontrado", 404
    if("nome_usuario" in body):
      rest.nome_usuario = body["nome_usuario"]
    if("email_usuario" in body):
      rest.email_usuario = body["email_usuario"]
    if("senha_usuario" in body):
      rest.senha_usuario = body["senha_usuario"]
    if("id_taxis" in body):
      rest.id_taxis = body["id_taxis"]
    if("tipo_usuario" in body):
      rest.tipo_usuario = body["tipo_usuario"]
    
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415
