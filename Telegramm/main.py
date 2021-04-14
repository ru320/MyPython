############# Imports
import Telegram as TG
import requests, json

############# Variablen
#- Landkreis HDH
URL = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=GEN%20%3D%20%27HEIDENHEIM%27&outFields=GEN,last_update,cases7_per_100k_txt&returnGeometry=false&outSR=&f=json"

inzidenzen = requests.get(URL).json()
last_update = inzidenzen['features'][0]['attributes']['last_update']
nachricht = ""

############# Nachricht vorbereiten

#- Datum holen
nachricht = f'Stand: {last_update}\n\n'

#- Durchlauf durch Json
for inzidenz in inzidenzen['features']:
    landkreis = inzidenz['attributes']['GEN']
    inz = inzidenz['attributes']['cases7_per_100k_txt']
    nachricht += f'{inz}\t {landkreis}\n'

############# NAchricht Senden
print(TG.SendMultTelegram(nachricht))
