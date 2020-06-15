'''
8 - Faça um Programa que pergunte quanto você ganha por mês e o número de horas trabalhadas no mês.
Calcule e mostre o salário por dia e por hora.
'''
valor = str(input('Qual o valor do seu salário em R$: ')).replace(',', '.')
salario = float(valor)
horas = int(input('Insira o total de horas trabalhadas por semana: '))
dia = int(input('Informe o total de dias trabalhados no mês: '))

horasporsemana = horas * 5    # horas trabalhadas por mês
salpordia = salario / dia     # saláro por dia
salporhora = salario / horas  # salário por hora

print(f'Para o trabalhador atue {horasporsemana} horas mês ele irá receber:')
print(f'Salário informado: {salario:.2f}')
print(f'Salário por hora: {salporhora:.2f}')
print(f'Salário por dia: {salpordia:.2f}')
