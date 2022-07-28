from config import db

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

