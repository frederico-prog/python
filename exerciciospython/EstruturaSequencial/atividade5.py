'''
5 - Faça um Programa que converta metros para centímetros.
'''
valor = str(input('Insira o valor em metros: ')).replace(',', '.')
metros = float(valor)
centimetros = metros * 100

print(f'O valor {metros}m convertido para centímetros é: {centimetros}cm')