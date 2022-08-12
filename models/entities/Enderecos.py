from config import db

class Enderecos(db.Model):
    id_endereco = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(30))
    estado = db.Column(db.String(30))
    rua = db.Column(db.String(30))
    bairro = db.Column(db.String(30))
    numero = db.Column(db.String(10))
    
    def to_json(self):
        return {
            "id_endereco": self.id_endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "rua": self.rua,
            "bairro": self.bairro,
            "numero": self.numero
        }