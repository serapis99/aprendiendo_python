from urllib.request import urlopen
import json

url="https://random-data-api.com/api/address/random_address?size=2"

# se realiza la peticion 
response=urlopen(url)

# se transforma los datos optenidos a un diccionario
data=json.loads(response.read())

# se recorre los datos y se procesa como diccionario
for persona in data:
    print("la direccion completa es:",persona['full_address'])
