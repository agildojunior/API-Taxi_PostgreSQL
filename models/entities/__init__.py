from .Empresas import Empresas
from .Taxis import Taxis
from .Corridas import Corridas
from .Usuarios import Usuarios
from config import db

__all__ = [
  'Empresas',
  'Taxis',
  'Corridas',
  'Usuarios',
]

db.create_all()