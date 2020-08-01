'''
41 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
'''
juros = parcela = 0
valor = float(input('Informe o valor da dívida: '))

for i in range(1, 13):
    if i == 1:
        print(f'À vista: {valor}')
    if i == 3:
        valor_atualizado = valor + (valor * 0.10)
        parcela = valor / i
        print(f'Valor da dívida com 10% de aumento: {valor_atualizado}\nNúmero de parcelas: {i}\n'
              f'Valor da parcela: {parcela:.2f}')
    if i == 6:
        valor_atualizado = valor + (valor * 0.15)
        parcela = valor / i
        print(f'Valor da dívida com 15% de aumento: {valor_atualizado}\nNúmero de parcelas: {i}\n'
              f'Valor da parcela: {parcela:.2f}')
    if i == 9:
        valor_atualizado = valor + (valor * 0.20)
        parcela = valor / i
        print(f'Valor da dívida com 20% de aumento: {valor_atualizado}\nNúmero de parcelas: {i}\n'
              f'Valor da parcela: {parcela:.2f}')
    if i == 12:
        valor_atualizado = valor + (valor * 0.25)
        parcela = valor / i
        print(f'Valor da dívida com 25% de aumento: {valor_atualizado}\nNúmero de parcelas: {i}\n'
              f'Valor da parcela: {parcela:.2f}')

