'''
REQUISIÇÕES PRINCIPAIS
get - pega a requisição
post - utilizado para enviar uma mensagem
'''

import requests  #Beautiful Soup 4 - BS4 - pip install bs4

cabecalho = {'User-agent': 'Windows 12', 'Referer': 'https://google.com'}
texto = None
meus_cookies = {'Ultima-visita': '10-10-2020'}
dados = {'username': 'guigui', 'password': 'guigui123'}

try:
    requisicao = requests.post('https://putsreq.com/KRMAnNIqkzYf4rSWLiAX', headers=cabecalho, cookies=meus_cookies, data=dados)
    texto = requisicao.text
except Exception as e:
    print('A requisição deu erro: ', e)

print(texto)