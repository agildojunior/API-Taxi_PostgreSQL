from config import db
from flask import jsonify, request

class Empresas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  cnpj = db.Column(db.String(50))

  def to_json(self):
    return {
      "id": self.id,
      "name": self.name,
      "cnpj": self.cnpj,
    }

#-----------------------------------------------------------------------------------

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
        name = body["name"],
        cnpj = body["cnpj"],
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
      if("name" in body):
        rest.name = body["name"]
      if("cnpj" in body):
        rest.cnpj = body["cnpj"]
      db.session.add(rest)
      db.session.commit()
      return "Atualizado com sucesso", 200
    return {"error": "Os dados devem ser JSON"}, 415

