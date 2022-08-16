from models import taxisModel

def get_all(current_empresa):
  return taxisModel.get_all(current_empresa)

def get_by_id(current_empresa,id):
  return taxisModel.get_by_id(current_empresa,id)

def insert(current_empresa):
  return taxisModel.insert(current_empresa)

def update(current_empresa,id):
  return taxisModel.update(current_empresa,id)
