from models import corridasModel

def get_all():
  return corridasModel.get_all()

def get_by_id(id):
  return corridasModel.get_by_id(id)

def insert():
  return corridasModel.insert()

def update(id):
  return corridasModel.update(id)
