from config import db
from flask import jsonify, request

class Taxis(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name_motorista = db.Column(db.String(50))

  def to_json(self):
    return {
      "id": self.id,
      "name_motorista": self.name_motorista,
    }

#-----------------------------------------------------------------------------------

  def get_all():
    rest = Taxis.query.all()
    return jsonify([taxis.to_json() for taxis in rest]), 200

  def get_by_id(id):
    rest = Taxis.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    return jsonify(rest.to_json())

  def insert():
    if request.is_json:
      body = request.get_json()
      res = Taxis (
        name_motorista = body["name_motorista"],
      )
      db.session.add(res)
      db.session.commit()
      return jsonify(res.to_json()) , 201
    return {"error": "Os dados devem ser JSON"}, 415

  def update(id):
    if request.is_json:
      body = request.get_json()
      rest = Taxis.query.get(id)
      if rest is None:
        return "Nao encontrado", 404
      if("name_motorista" in body):
        rest.name_motorista = body["name_motorista"]
      db.session.add(rest)
      db.session.commit()
      return "Atualizado com sucesso", 200
    return {"error": "Os dados devem ser JSON"}, 415
