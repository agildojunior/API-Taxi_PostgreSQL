from config import db

class Taxis(db.Model):
    id_taxis = db.Column(db.Integer, primary_key=True)
    nome_taxista = db.Column(db.String(50))
    telefone_taxista = db.Column(db.String(15))
    modelo_taxi = db.Column(db.String(50))
    placa_taxi = db.Column(db.String(50))
    ativo = db.Column(db.Boolean, default=True)
    
    def to_json(self):
      return {
          "id_taxis": self.id_taxis,
          "nome_taxista": self.nome_taxista,
          "telefone_taxista": self.telefone_taxista,
          "modelo_taxi": self.modelo_taxi,
          "placa_taxi": self.placa_taxi,
          "ativo": self.ativo         
      }
