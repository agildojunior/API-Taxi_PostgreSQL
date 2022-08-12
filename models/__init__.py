from .entities.Empresas import Empresas
from .entities.Taxis import Taxis
from .entities.Corridas import Corridas
from .entities.Usuarios import Usuarios
from .entities.Enderecos import Enderecos
from config import db

__all__ = [
  'Empresas',
  'Taxis',
  'Corridas',
  'Usuarios',
  'Enderecos',
]

db.create_all()