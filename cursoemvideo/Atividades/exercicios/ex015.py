# Escreva um programa que pergunte a quantidade de KM percorrida por um carro e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
print('******** DESAFIO - AULA 07 - CALCULAR ALUGUEL DE CARRO *********')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
