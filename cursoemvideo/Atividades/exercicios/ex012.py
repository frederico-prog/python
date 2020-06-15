# Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto
print('******** DESAFIO - AULA 07 - CALCULADORA 5 *********')
n1 = float(input('Digite o valor do produto: R$ '))
# vdesc = (n1 * 5 / 100)
desconto = n1 - (n1 * 5 / 100)
print('O novo valor do produto com 5% de desconto é R${:.2f}'.format(desconto))
