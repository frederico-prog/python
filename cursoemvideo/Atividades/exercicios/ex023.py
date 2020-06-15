'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
Ex.:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
'''
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}.'.format(num))
print('Unidade: {:2} \nDezena: {:2} \nCentena: {:2} \nMilhar: {:2}'.format(u, d, c, m))
