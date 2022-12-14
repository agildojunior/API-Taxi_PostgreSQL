from models import usuariosModel

def get_all(current_empresa):
  return usuariosModel.get_all(current_empresa)

def get_by_id(current_empresa,id):
  return usuariosModel.get_by_id(current_empresa,id)

def insert(current_empresa):
  return usuariosModel.insert(current_empresa)

def update(current_empresa,id):
  return usuariosModel.update(current_empresa,id)

def get_by_email(current_empresa,email):
  return usuariosModel.get_by_email(current_empresa,email)

def delete(current_empresa,id): 
  return usuariosModel.delete(current_empresa,id)