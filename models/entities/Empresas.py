from config import db

class Empresas(db.Model):
    id_empresa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    cnpj = db.Column(db.String(50))
    ativo = db.Column(db.Boolean, default=True)

    def to_json(self):
      return {
        "id_empresa": self.id_empresa,
        "nome": self.nome,
        "cnpj": self.cnpj,
        "ativo": self.ativo
      }

