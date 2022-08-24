from models import corridasModel

def get_all(current_empresa):
  return corridasModel.get_all(current_empresa)

def get_by_id(current_empresa,id):
  return corridasModel.get_by_id(current_empresa,id)

def insert(current_empresa):
  return corridasModel.insert(current_empresa)

def update(current_empresa,id):
  return corridasModel.update(current_empresa,id)

def delete(current_empresa,id): 
  return corridasModel.delete(current_empresa,id)

def get_by_id_empresa(current_empresa,id_empresa): 
  return corridasModel.get_by_id_empresa(current_empresa,id_empresa)

def get_corridas_report(id_empresa):
  return corridasModel.get_corridas_report(id_empresa)
