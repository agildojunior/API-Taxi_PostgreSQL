from models import taxisModel

def get_all():
  return taxisModel.get_all()

def get_by_id(id):
  return taxisModel.get_by_id(id)

def insert():
  return taxisModel.insert()

def update(id):
  return taxisModel.update(id)
