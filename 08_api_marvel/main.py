import hashlib
import requests
import json

from pprint import pprint

# creando variables de llaves
ts=1
private_key="3bfb490e5521a13a0b57537a2a60868984b695a1"
public_key="b9a0bde6bd617a13c0e56905603b052f"

# creando codigo hash md5
codigo=hashlib.md5(str(ts).encode()+private_key.encode()+public_key.encode())
hash=codigo.hexdigest()

#creando la url a consultar
payload={
    'ts':ts,
    'apikey':public_key,
    'hash':hash
}
url="https://gateway.marvel.com:443/v1/public/characters"

# se permite el redireccionamiento ya que sin este genera error
response=requests.get(url,params=payload,allow_redirects=True)

if response.status_code==200:
    datos=json.loads(response.text)
    # pprint(datos['data']['results'][0])

    for row in datos['data']['results']:
        
        print("nombre : {0} descripcion: {1} historias: {2} series: {3} ".format(row['name'], 
                                                                                 row['description'], 
                                                                                 row['stories']['returned'], 
                                                                                 row['series']['returned']
                                                                                 ))
