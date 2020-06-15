'''
API - API OpenWeathMap

EXERCICIOS
- Faça um programa que verifique o tempo em tempo real
'''
import requests
import json

cidade = str(input('Escreva a sua cidade: ')).lower().strip()
key = 'e08ec0704a7b6aad839e39028eb40f5a'

print('-' * 20 + ' PREVISÃO DO TEMPO ' + '-' * 20)
try:
    requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=' + key)
    tempo = json.loads(requisicao.text)
    temperatura = float(tempo['main']['temp']) - 273.15
    print('Condição do tempo: ', tempo['weather'][0]['main'])
    print('Temperatura: ', '%.2f' % temperatura)
except Exception as e:
    print('Ocorreu um erro. Procurar o administrador. ', e)
