'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.
'''
print('***** CALCULAR SALÁRIO *****')
salario = float(input('Entre com o salário do coladorador: R$ '))
nome = str(input('Entre com o nome do funcionário: ')).strip()
base = 1250.00
if salario <= base:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("O novo salário do colaborador {} será de R$ {:.2f}".format(nome, novo))
