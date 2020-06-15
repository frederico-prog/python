# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
print('******** DESAFIO - AULA 08 - CALCULAR A HIPOTENUSA DE UM TRIÂNGULO *********')
from math import sqrt, hypot
'''PRIMEIRA OPÇÃO'''
catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))
calculo = pow(catadjacente, 2) + pow(catoposto, 2)
hip = sqrt(calculo)
print('A hipotenusa vai medir {:.3f}'.format(hip))

'''SEGUNDA OPÇÃO'''
hi = (catoposto ** 2 + catadjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.3f}'.format(hi))

'''TERCEIRA OPÇÃO'''
hi2 = hypot(catoposto, catadjacente)
print('A hipotenusa vai medir {:.3f}'.format(hi2))
