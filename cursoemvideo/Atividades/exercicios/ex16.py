# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex.: Digite o nº: 6.127. O número tem a parte inteira 6
print('******** DESAFIO - AULA 08 - RETORNAR A PARTE INTEIRA DE UM Nº *********')
from math import trunc
num = float(input('Digite um número: '))
print('A parte inteira do número {} é o número {}.'.format(num, trunc(num)))

print('UMA OUTRA OPÇÃO PARA RESOLVER O PROBLEMA')
print('A parte inteira do número {} é o número {}.'.format(num, int(num)))
