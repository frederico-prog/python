'''
22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão).
'''
num = float(input('Informe um valor inteiro. '))

if num % 2 == 0:
    print('É par')
elif num % 2 > 0:
    print('É ímpar')
else:
    print('Erro no valor digitado.')