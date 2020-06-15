'''
8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''
valor = str(input('Informe o seu salário por hora: ')).replace(',', '.')
horas = int(input('Informe o número de horas trabalhadas por mês: '))
salario = float(valor)

totalmes = salario * horas

print(f'O seu salário este mês será de R$ {totalmes:.2f}')