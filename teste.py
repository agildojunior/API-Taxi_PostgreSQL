import requests, json

a = {"name":"teste123","cnpj":"6666666666"}

res=requests.put('http://127.0.0.1:8090/empresas/4',json=a)

