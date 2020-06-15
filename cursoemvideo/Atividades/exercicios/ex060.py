'''
Faça um programa que leia um nº qualquer e mostre o seu fatorial.
Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from math import factorial
print('-=-' * 20)
print('{:^60}'.format(' SISTEMA DE CÁLCULO DE FATORIAL '))
print('-=-' * 20)

num = int(input('Insira o valor desejado: '))
c = num
f = 1
print(' Calculando {}! = '.format(num), end='')

while c > 0:
    print('{} '.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''
f = factorial(num)
print('O fatorial do número {}! é {}'.format(num, f))
'''

'''
fatorial = 1
for count in range(num, 0, -1):
    fatorial = count * fatorial
    #print(count, end='→ ')
print('\nO fatorial de {}! = {}'.format(num, fatorial))
'''
