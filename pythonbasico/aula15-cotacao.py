'''
API - API Awesomeapi

EXERCICIOS
- Faça o programa a cotação do dolar em tempo real
'''

import requests
import json
import time

while True:
    try:
        requisicao = requests.get('https://economia.awesomeapi.com.br/all')
        cotacao = json.loads(requisicao.text)
        print('-' * 20 + ' COTAÇÃO ' + '-' * 20)
        print('ÚLTIMA CONSULTA: ' + cotacao['USD']['create_date'])
        print('DÓLAR: ' + cotacao['USD']['bid'])
        print('EURO: ' + cotacao['EUR']['bid'])
        print('BTC: ' + cotacao['BTC']['bid'])
    except Exception as e:
        print('Ocorreu um erro. Procure o administrador do sistema. ', e)
    time.sleep(2)
