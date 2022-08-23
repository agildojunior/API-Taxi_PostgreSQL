from flask import jsonify, request
from .entities import Corridas
from config import db
from pycep_correios import get_address_from_cep, WebService, exceptions
import googlemaps
import re
import sys

api_key = 'AIzaSyA2q035Meede4sQ6jde84BGysxvXpDalmI'

def get_all(current_empresa):
  rest = Corridas.query.all()
  return jsonify([corridas.to_json() for corridas in rest]), 200

def get_by_id(current_empresa,id):
  rest = Corridas.query.get(id)
  if rest is None:
    return "Nao encontrado", 404
  return jsonify(rest.to_json())

def insert(current_empresa):
  if request.is_json:
    body = request.get_json()
    res = Corridas (
      # origem = body['origem'],
      # destino = body['destino'],
      # nome_usuario = None,
      # id_empresa = None,
      # id_taxi = None,
    )
    
    if('cep_origem' in body and 'cep_destino' in body):
      cepOrigem = trataCep(body['cep_origem'])
      cepDestino = trataCep(body['cep_destino'])
      
      if (verificaCep(cepOrigem) == ''):
          
          return {"error": "CEP origem inválido"}, 400
      elif(verificaCep(cepDestino) == ''):
          
          return {"error": "CEP destino inválido"}, 400
      else:
          cepOrigemNumber = verificaCep(cepOrigem)
          cepDestinoNumber = verificaCep(cepDestino)
          
          valorCorrida = calculaCorrida(cepOrigemNumber, cepDestinoNumber)

          res.cep_origem = cepOrigemNumber
          res.cep_destino = cepDestinoNumber
          res.preco = valorCorrida
      
    if("origem" in body):
      res.origem = body["origem"]
    if("destino" in body):
      res.destino = body["destino"]
    if("status" in body):
      res.status = body["status"]
    if("nome_usuario" in body):
      res.nome_usuario = body["nome_usuario"]
    if("id_empresa" in body):
      res.id_empresa = body["id_empresa"]
    if("id_taxi" in body):
      res.id_taxi = body["id_taxi"]
      
    db.session.add(res)
    db.session.commit()
    
    return jsonify(res.to_json()) , 201
  return {"error": "Os dados devem ser JSON"}, 415

def update(current_empresa,id):
  if request.is_json:
    body = request.get_json()
    rest = Corridas.query.get(id)
    if rest is None:
      return "Nao encontrado", 404
    if("origem" in body):
      rest.origem = body["origem"]
    if("destino" in body):
      rest.destino = body["destino"]
    if("status" in body):
      rest.status = body["status"]
    if("nome_usuario" in body):
      rest.nome_usuario = body["nome_usuario"]

    if("id_taxi" in body):
      rest.id_taxi = body["id_taxi"]
    
    db.session.add(rest)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Os dados devem ser JSON"}, 415

#Relatorios
def get_by_id_empresa(current_empresa,id_empresa):
  rest = Corridas.query.filter_by(id_empresa=id_empresa).all()
  if rest is None:
    return "Não encontrado", 404
  return jsonify([corridas.to_json() for corridas in rest]), 200
  

def delete(current_empresa,id):
  rest = Corridas.query.get(id)
  if rest is None:
      return {"error": {"error": "Nao encontrado"}}, 404
  rest.ativo = False
  db.session.add(rest)
  db.session.commit()
  return {"message": "Deletado com sucesso"}, 200




####################################################

def trataCep(cep):
    try:
      if(len(cep) < 8):
          
          return {"error": "CEP inválido"}, 400
          
      else:
          
          cepNumbers = re.sub(r"[^0-9]","", cep)
          #retira caracteres especiais e letras, deixando apenas números
          cepTratado = str(cepNumbers[0:8])
    except:
      return {"error": 'CEP inválido'}, 400
    return cepTratado

def verificaCep(cepRecebido):
    try:
        cep = get_address_from_cep(cepRecebido, webservice=WebService.CORREIOS)
        cidadeCep = cep['cidade']
        
    except exceptions.InvalidCEP as eic:
        return {"error": eic}, 400

    except exceptions.CEPNotFound as ecnf:
        return {"error": ecnf}, 400

    except exceptions.ConnectionError as errc:
        return {"error": errc}, 400
      
    except exceptions.Timeout as errt:
        return {"error": errt}, 400

    except exceptions.HTTPError as errh:
        return {"error": errh}, 400

    except exceptions.BaseException as e:
        return {"error": e}, 400
        
    return cidadeCep

def calculaCorrida(origem, destino):   
    gmaps = googlemaps.Client(key=api_key) 
    my_dist = gmaps.distance_matrix(origem,destino)['rows'][0]['elements'][0] 
    
    
    distancia = my_dist['distance']
    valorDistancia = distancia['value']
    
    valorKm = int(2.50 * (valorDistancia / 1000) + 10)
    
    return valorKm
    
