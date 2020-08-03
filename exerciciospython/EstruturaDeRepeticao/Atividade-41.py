'''
41 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''
from datetime import date
from time import sleep

juros = parcela = 0
data_atual = date.today()

valor_str = str(input(f'Informe o valor da dívida em {data_atual}: ')).replace(',', '.')
valor = float(valor_str)

print('Tabela de Juros')
print('Parcela\t Taxa de juros')
for t in range(1, 13):
    if t == 1:
        print(f'{t}\t\t\t 0%')
    if t == 3:
        print(f'{t}\t\t\t 10%')
    if t == 6:
        print(f'{t}\t\t\t 15%')
    if t == 9:
        print(f'{t}\t\t\t 20%')
    if t == 12:
        print(f'{t}\t\t\t 25%')

print('Calculando parcelas...')
sleep(1)
print('Valor da dívida\t Valor dos juros\t\t Quantidade de parcelas\t\t Valor da parcela')

for i in range(1, 13):
    if i == 1:
        print(f'R$ {valor:.2f}\t\t\t R$ {juros:.2f}\t\t\t\t\t\t {i}\t\t\t\t\t R$ {valor:.2f}')
    if i == 3:
        juros = valor * 0.10
        valor_atualizado = valor + juros
        parcela = valor_atualizado / i
        print(f'R$ {valor_atualizado:.2f}\t\t\t R$ {juros:.2f}\t\t\t\t\t\t {i}\t\t\t\t\t R$ {parcela:.2f}')
    if i == 6:
        juros = valor * 0.15
        valor_atualizado = valor + juros
        parcela = valor_atualizado / i
        print(f'R$ {valor_atualizado:.2f}\t\t\t R$ {juros:.2f}\t\t\t\t\t\t {i}\t\t\t\t\t R$ {parcela:.2f}')
    if i == 9:
        juros = valor * 0.20
        valor_atualizado = valor + juros
        parcela = valor_atualizado / i
        print(f'R$ {valor_atualizado:.2f}\t\t\t R$ {juros:.2f}\t\t\t\t\t\t {i}\t\t\t\t\t R$ {parcela:.2f}')
    if i == 12:
        juros = valor * 0.25
        valor_atualizado = valor + juros
        parcela = valor_atualizado / i
        print(f'R$ {valor_atualizado:.2f}\t\t\t R$ {juros:.2f}\t\t\t\t\t\t {i}\t\t\t\t\t R$ {parcela:.2f}')


