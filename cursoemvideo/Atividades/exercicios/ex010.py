# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ele pode comprar.
# Considere US$1,00 = R$3,27 - US$ = 5,10 - € = 5,70
print('******** DESAFIO - AULA 07 - CALCULADORA 3 *********')
n1 = float(input('Quanto você quer investir na compra dos dólares? R$ '))
cotacao = float(input('Digite a cotação do dólar atualmenete: US$ '))
cotacao1 = float(input('Digite a cotação do euro atualmente: € '))
dolar = n1 / cotacao
euro = n1 / cotacao1
print('Com o valor de R$ {:.2f} você pode comprar US$ {:.2f} e € {:.2f}.'.format(n1, dolar, euro))
