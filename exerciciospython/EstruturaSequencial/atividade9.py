'''
9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
Formula: C = (5 * (F-32) / 9).
'''
valor = str(input('Informe a temperatura em Farenheit: ')).replace(',', '.')
farenheit = float(valor)
celsius = (5 * (farenheit - 32) / 9)

print(f'Para a temperatura digitada, o seu valor em Celsius é de {celsius}ºC')
