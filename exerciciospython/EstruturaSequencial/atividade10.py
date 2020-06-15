'''
10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''
valor = str(input('Informe a temperatura em Celsius: ')).replace(',', '.')
celsius = float(valor)
farenheit = (celsius * 9 / 5 ) + 32

print(f'Para a temperatura digitada, o seu valor em Celsius é de {farenheit}ºF')