import requests
import pprint

api_key = "65072fed03ff4fba9a7193613261901"
api_link = "http://api.weatherapi.com/v1/current.json"

parametros= {
    "key": api_key,
    "q": "Japan",        
    "lang": "pt",   
}

resposta = requests.get(api_link, params=parametros)

if resposta.status_code == 200:
    requisitado = resposta.json()
    pprint.pprint(requisitado)
    temp = requisitado['current']['condition']['text']
    print(temp)