from config import db

class Corridas(db.Model):
    id_corrida = db.Column(db.Integer, primary_key=True)
    origem = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    # horario = db.Column(db.DateTime, server_default=db.func.now())
    status = db.Column(db.String(30), default = 'Solicitada')
    nome_usuario = db.Column(db.String(100),nullable=True)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id_empresa'),nullable=True)
    id_taxi = db.Column(db.Integer, db.ForeignKey('taxis.id_taxis'),nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
  
    def to_json(self):
      return {
        "id_corrida": self.id_corrida,
        "origem": self.origem,
        "destino": self.destino,
        # "horario": self.horario,
        "status": self.status,
        "nome_usuario": self.nome_usuario,
        "id_empresa": self.id_empresa,
        "id_taxi": self.id_taxi,
        "created_at": self.created_at
      }

