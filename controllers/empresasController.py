from models import empresasModel

def get_all():
  return empresasModel.get_all()

def get_by_id(id):
  return empresasModel.get_by_id(id)

def insert():
  return empresasModel.insert()

def update(id):
  return empresasModel.update(id)
