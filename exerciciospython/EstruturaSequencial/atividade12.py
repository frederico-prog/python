'''
12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
'''
valor = str(input('Informe a sua altura em metros: ')).replace(',', '.')
altura = float(valor)

pesoideal = (72.7 * altura) - 58

print(f'Para a altura de {altura}m, o peso ideal é {pesoideal:.2f}kg')
