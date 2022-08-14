from flask import jsonify, request
from .entities import Usuarios
from config import db

def get_all():
  rest = Usuarios.query.all()
  return jsonify([usuarios.to_json() for usuarios in rest]), 200

def get_by_id(id):
  rest = Usuarios.query.get(id)
  if rest is None:
    return "Não encontrado", 404
  return jsonify(rest.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    res = Usuarios (
        nome_usuario = body['nome_usuario'],
        email_usuario = body["email_usuario"],
        senha_usuario = body["senha_usuario"],
        id_empresa = body["id_empresa"],
        id_taxis = body["id_taxis"]
    )
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(id):
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
    if("id_empresa" in body):
      rest.id_empresa = body["id_empresa"]
    if("id_taxis" in body):
      rest.id_taxis = body["id_taxis"]
    
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415
