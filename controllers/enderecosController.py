from models import enderecosModel

def get_all():
  return enderecosModel.get_all()

def get_by_id(id):
  return enderecosModel.get_by_id(id)

def insert():
  return enderecosModel.insert()

def update(id):
  return enderecosModel.update(id)
