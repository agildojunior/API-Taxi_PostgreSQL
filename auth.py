import jwt
from flask import jsonify , request
from functools import wraps
from models import entities
from config import app

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
      token = None
      if 'x-access-token' in request.headers:
          token = request.headers['x-access-token']
      if not token:
          return jsonify({'message' : 'Token is missing!'}), 401
      try: 
          data = jwt.decode(token, app.config['SECRET_KEY'], options={'verify_signature': False})
          current_empresa = entities.Empresas.query.filter_by(cnpj = data['cnpj']).first()
      except:
          return jsonify({'message' : 'Token is invalid!'}), 401
      return f(current_empresa, *args, **kwargs)
  return decorated