from config import db

class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100))
    email_usuario = db.Column(db.String(100), unique = True)
    senha_usuario = db.Column(db.String(100))
    ativo = db.Column(db.Boolean, default=True)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id_empresa'))
    
    def to_json(self):
        return {
            "id_usuario": self.id_usuario,
            "nome_usuario": self.nome_usuario,
            "email_usuario": self.email_usuario,
            "senha_usuario": self.senha_usuario,
            "ativo": self.ativo,
            "id_empresa": self.id_empresa
        }