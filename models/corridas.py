from config import db

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

