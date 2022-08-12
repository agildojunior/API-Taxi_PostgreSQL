from .Empresas import Empresas
from .Taxis import Taxis
from .Corridas import Corridas
from .Usuarios import Usuarios
from .Enderecos import Enderecos
from config import db

__all__ = [
  'Empresas',
  'Taxis',
  'Corridas',
  'Usuarios',
  'Enderecos',
]

db.create_all()