'''
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
    a - salário bruto.
    b - quanto pagou ao INSS.
    c - quanto pagou ao sindicato.
    d - o salário líquido.
    e - calcule os descontos e o salário líquido, conforme a tabela abaixo
'''
valor = str(input('Informe o seu salário por hora: ')).replace(',', '.')
horas = int(input('Informe o número de horas trabalhadas por mês: '))
salario = float(valor)

totalmes = salario * horas      # salário bruto
inss = totalmes * 0.11
insssindicato = totalmes * 0.08
sindicato = totalmes * 0.05
salliquido = totalmes - (inss + insssindicato + sindicato)

print(f'Salário bruto: R$ {totalmes:.2f}')  # 2717.00
print(f'INSS(11%): R$ {inss:.2f}')
print(f'INSS Sindicato(8%): R$ {insssindicato:.2f}')
print(f'Sindicato(5%): R$ {sindicato:.2f}')
print(f'Salário líguido: R$ {salliquido:.2f}')
