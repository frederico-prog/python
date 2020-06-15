'''
16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    a- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
    pedir os demais valores, sendo encerrado;
    b- Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    c- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    d- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

print('-' * 20 + ' SISTEMA PARA CALCULO DE EQUAÇÃO DO SEGUNDO GRAU ' + '-' * 20)

valor = str(input('Informe o valor de "A": ')).replace(',', '.')
valor1 = str(input('Informe o valor de "B": ')).replace(',', '.')
valor2 = str(input('Informe o valor de "C": ')).replace(',', '.')

if valor == '':
    a = 1
else:
    a = float(valor)

if valor1 == '':
    b = 1
else:
    b = float(valor1)

if valor2 == '':
    c = 1
else:
    c = float(valor2)

# Imprime a expressão na tela
print('Expressão: ', end='')
if b < 0:
    print(f'{a:.2f}x² {b:.2f}x + {c:.2f} = 0')
else:
    print(f'{a:.2f}x² + {b:.2f}x + {c:.2f} = 0')

# Verificar se o valor de "A" é igual a zero e encerra o programa assim que identificado
if a == '':
    a = 1
elif a == 0:
    print('A equação não é do segundo grau e o programa não pode ser executada.')

# Realização do cálculo
delta = pow(b, 2) - 4 * a * c

if delta < 0:
    print('A expressão não possui raiz.')
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print(f'A raiz da equação é: {raiz}')
else:
    raiz1 = (-1 * b - math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b + math.sqrt(delta)) / (2 * a)
    print(f'A raiz da equação são: {raiz1} e {raiz2}')

