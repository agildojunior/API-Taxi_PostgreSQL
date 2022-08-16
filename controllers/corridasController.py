from models import corridasModel

def get_all(current_empresa):
  return corridasModel.get_all(current_empresa)

def get_by_id(current_empresa,id):
  return corridasModel.get_by_id(current_empresa,id)

def insert(current_empresa):
  return corridasModel.insert(current_empresa)

def update(current_empresa,id):
  return corridasModel.update(current_empresa,id)
