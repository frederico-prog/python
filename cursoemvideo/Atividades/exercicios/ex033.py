'''
Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
'''
print('***** VERIFICA O MAIOR E MENOR NÚMERO *****')
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O maior número é {:.2f} e o menor número é o {:.2f}'.format(maior, menor))
