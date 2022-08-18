from config import db

class Taxis(db.Model):
    id_taxis = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    telefone_taxista = db.Column(db.String(15))
    modelo_taxi = db.Column(db.String(50))
    placa_taxi = db.Column(db.String(50))
    ativo = db.Column(db.Boolean, default=True)
    
    def to_json(self):
      return {
          "id_taxis": self.id_taxis,
          "id_usuario": self.id_usuario,
          "telefone_taxista": self.telefone_taxista,
          "modelo_taxi": self.modelo_taxi,
          "placa_taxi": self.placa_taxi,
          "ativo": self.ativo         
      }
