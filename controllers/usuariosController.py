from models import usuariosModel

def get_all():
  return usuariosModel.get_all()

def get_by_id(id):
  return usuariosModel.get_by_id(id)

def insert():
  return usuariosModel.insert()

def update(id):
  return usuariosModel.update(id)
