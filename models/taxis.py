from config import db

class Taxis(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name_motorista = db.Column(db.String(50))

  def to_json(self):
    return {
      "id": self.id,
      "name_motorista": self.name_motorista,
    }
