'''
7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
import math

valor = str(input('Insira o valor do lado do quadrado: ')).replace(',', '.')
parservalor = float(valor)

area = pow(parservalor, 2)
dobroarea = area * 2

print(f'A área do quadrado é {area:.2f}cm e o seu dobro é {dobroarea:.2f}cm')
