'''
Faça um programa que leia um ano qualquer e mostre se ele pe BISSEXTO
'''
from datetime import date
print('***** CALCULAR ANO BISSEXTO *****')
ano = int(input('Digite o ano que deseja analisar: Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO!'.format(ano))

'''
elif ano % 4 == 0 and ano % 100 != 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
'''