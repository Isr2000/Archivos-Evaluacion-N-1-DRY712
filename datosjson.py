#ANALISIS DE FORMATO PUNTO 1  ITEM C
#ANALISIS DE FORMATO PUNTO 1  ITEM C
import json
import yaml
with open('myfile.json','r') as json_file:
    ourjson=json.load(json_file)
print(ourjson)
print("El token de acceso es: {}".format(ourjson['access_token']))
print("El token expira en {} segundos.".format(ourjson['expires_in']))
