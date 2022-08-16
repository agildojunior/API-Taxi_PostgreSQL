from models import empresasModel

def get_all(current_empresa):
  return empresasModel.get_all(current_empresa)

def get_by_id(current_empresa,id):
  return empresasModel.get_by_id(current_empresa,id)

def insert(current_empresa):
  return empresasModel.insert(current_empresa)

def update(current_empresa,id):
  return empresasModel.update(current_empresa,id)
