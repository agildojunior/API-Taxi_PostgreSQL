from models import enderecosModel

def get_all(current_empresa):
  return enderecosModel.get_all(current_empresa)

def get_by_id(current_empresa,id):
  return enderecosModel.get_by_id(current_empresa,id)

def insert(current_empresa):
  return enderecosModel.insert(current_empresa)

def update(current_empresa,id):
  return enderecosModel.update(current_empresa,id)
