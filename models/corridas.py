from config import db
from flask import jsonify, request

class Corridas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id'))
  id_taxis = db.Column(db.Integer, db.ForeignKey('taxis.id'))
  status_corrida = db.Column(db.String(50))
  cliente = db.Column(db.String(50))
  destino = db.Column(db.String(100))
  origem = db.Column(db.String(100))

  def to_json(self):
    return {
      "id": self.id,
      "id_empresa": self.id_empresa,
      "id_taxis": self.id_taxis,
      "status_corrida": self.status_corrida,
      "cliente": self.cliente,
      "destino": self.destino,
      "origem": self.origem,
    }

#-----------------------------------------------------------------------------------

  def get_all():
    rest = Corridas.query.all()
    return jsonify([corridas.to_json() for corridas in rest]), 200

  def get_by_id(id):
    rest = Corridas.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    return jsonify(rest.to_json())

  def insert():
    if request.is_json:
      body = request.get_json()
      res = Corridas (
        id_empresa = body["id_empresa"],
        id_taxis = body["id_taxis"],
        status_corrida = body["status_corrida"],
        cliente = body["cliente"],
        destino = body["destino"],
        origem = body["origem"],
      )
      db.session.add(res)
      db.session.commit()
      return jsonify(res.to_json()) , 201
    return {"error": "Os dados devem ser JSON"}, 415

  def update(id):
    if request.is_json:
      body = request.get_json()
      rest = Corridas.query.get(id)
      if rest is None:
        return "Nao encontrado", 404
      if("id_empresa" in body):
        rest.id_empresa = body["id_empresa"]
      if("id_taxis" in body):
        rest.id_taxis = body["id_taxis"]
      if("status_corrida" in body):
        rest.status_corrida = body["status_corrida"]
      if("cliente" in body):
        rest.cliente = body["cliente"]
      if("destino" in body):
        rest.destino = body["destino"]
      if("origem" in body):
        rest.origem = body["origem"]
      
      db.session.add(rest)
      db.session.commit()
      return "Atualizado com sucesso", 200
    return {"error": "Os dados devem ser JSON"}, 415
