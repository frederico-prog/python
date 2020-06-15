'''
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
valor = str(input('Informe o número desejado: ')).replace(',', '.')
num = float(valor)

if num > 0:
    print(f'O número {num:.2f} é positivo.')
else:
    print(f'O número {num:.2f} é negativo.')
