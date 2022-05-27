import requests
import json

cotaçoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL") #Requisição GET
cotaçoes = cotaçoes.json()
cotaçao_dolar = cotaçoes['USDBRL']['bid']
print(cotaçoes)
print(cotaçao_dolar)