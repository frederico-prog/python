'''
13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    a - Para homens: (72.7*h) - 58
    b - Para mulheres: (62.1*h) - 44.7
'''
valor = str(input('Informe a altura em metros: ')).replace(',', '.')
altura = float(valor)

homens = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

print(f'Para a altura digitada, o peso ideal para homens e mulheres é:')
print(f'Homens: {homens:.2f}')
print(f'Mulheres: {mulher:.2f}')
