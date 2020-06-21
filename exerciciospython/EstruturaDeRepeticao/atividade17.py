'''
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
print('-=-' * 20)
print('{:^60}'.format(' SISTEMA DE CÁLCULO DE FATORIAL '))
print('-=-' * 20)

num = int(input('Insira o valor desejado: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')

while c > 0:
    print('{} '.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


'''
from math import factorial

num = int(input('Informe o número desejado: '))
fatorial = factorial(num)
print(fatorial)
'''
