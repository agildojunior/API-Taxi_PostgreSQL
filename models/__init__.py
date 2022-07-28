from .empresas import Empresas
from .taxis import Taxis
from .corridas import Corridas
from config import db

__all__ = [
  'Empresas',
  'Taxis',
  'Corridas'
]

db.create_all()