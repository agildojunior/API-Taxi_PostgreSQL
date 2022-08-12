import requests, json

a = {"id_empresa":"1","id_taxis":"1","status_corrida":"aguardando","cliente":"teste","destino":"teste","origem":"teste"}

res=requests.post('http://127.0.0.1:8090/corridas',json=a)

