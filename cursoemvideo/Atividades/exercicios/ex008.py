# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
print('******** DESAFIO - AULA 07 - CONVERSÃO *********')
n1 = float(input('Digite o valor em metros: '))
cm = n1 * 100
mm = n1 * 1000
print('O valor {}m convertido para centímetros é {}cm e milímetros é {}mm.'.format(n1, cm, mm))
