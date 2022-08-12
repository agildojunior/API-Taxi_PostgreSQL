from flask import jsonify, request
from .entities import Enderecos
from config import db

def get_all():
  rest = Enderecos.query.all()
  return jsonify([enderecos.to_json() for enderecos in rest]), 200

def get_by_id(id):
  rest = Enderecos.query.get(id)
  if rest is None:
    return "Não encontrado", 404
  return jsonify(rest.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    res = Enderecos (
        cidade = body["cidade"],
        estado = body["estado"],
        rua = body["rua"],
        bairro = body["bairro"],
        numero = body["numero"]
    )
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(id):
  if request.is_json:
    body = request.get_json()
    rest = Enderecos.query.get(id)
    if rest is None:
      return "Não encontrado", 404
    if("cidade" in body):
      rest.cidade = body["cidade"]
    if("estado" in body):
      rest.estado = body["estado"]
    if("rua" in body):
      rest.rua = body["rua"]
    if("bairro" in body):
      rest.bairro = body["bairro"]
    if("numero" in body):
      rest.numero = body["numero"]
    
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415
