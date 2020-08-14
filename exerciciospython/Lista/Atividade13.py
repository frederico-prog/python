'''
13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
import random

lista_mes = [
    'JANEIRO',
    'FEVEREIRO',
    'MARÇO',
    'ABRIL',
    'MAIO',
    'JUNHO',
    'JULHO',
    'AGOSTO',
    'SETEMBRO',
    'OUTUBRO',
    'NOVEMBRO',
    'DEZEMBRO'
]

soma_temperatura = media_anual = 0
lista_temperatura = []

# Preenche a lista com as médias por mês e seus respectivos meses de forma randômica
for mes in lista_mes:
    lista_mes_temperatura = []
    temperatura = random.uniform(0.0, 50.0)
    lista_mes_temperatura.append(mes)
    lista_mes_temperatura.append(temperatura)
    lista_temperatura.append(lista_mes_temperatura)

# Verifica a média anual das temperaturas
for temp in lista_temperatura:
    soma_temperatura += temp[1]

media_anual = soma_temperatura / len(lista_temperatura)

# Verifica quais são os meses e as temperaturas acima da média anual
print(f'As temperaturas acima da média anual que foi de {media_anual:.2f}ºC são:')
for temp in lista_temperatura:
    if temp[1] > media_anual:
        print(f'{temp[0]} - {temp[1]:.2f}ºC')



