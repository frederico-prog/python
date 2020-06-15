import math
'''
11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a - o produto do dobro do primeiro com metade do segundo .
    b - a soma do triplo do primeiro com o terceiro.
    c - o terceiro elevado ao cubo.
'''

print('Informe 2 números inteiros e um número real:')
num1 = int(input('Informe o primeiro número inteiro: '))
num2 = int(input('Informe o segundo número inteiro: '))
valor = str(input('Informe o número real: ')).replace(',', '.')
num3 = float(valor)

produto = (num1 * 2 * num2 / 2)
soma = num1 * 3 + num3
cubo = pow(num3, 3)

print(f'O produto do dobro do primeiro com a metade do segundo: {produto}')
print(f'A soma do triplo do primeiro com o terceiro {soma}')
print(f'O terceiro elevado ao cubo {cubo:.2f}')
