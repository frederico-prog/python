'''
6- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
import math

pi = 3.14
valor = str(input('Informe o raio do cículo em metros: ')).replace(',', '.')
raio = float(valor)
area = pi * pow(raio, 2)
print(f'A área do círculo que possui {raio:.2f}m é de: {area:.2f}')
