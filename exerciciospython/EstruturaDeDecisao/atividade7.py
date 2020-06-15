'''
7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
num1 = str(input('Insira o primeiro número: ')).replace(',', '.')
num2 = str(input('Insira o segundo número: ')).replace(',', '.')
num3 = str(input('Insira o terceiro número: ')).replace(',', '.')

parsernum1 = float(num1)
parsernum2 = float(num2)
parsernum3 = float(num3)

maior = parsernum1
menor = parsernum1

if parsernum2 > maior:
    maior = parsernum2
if parsernum3 > maior:
    maior = parsernum3
if parsernum2 < menor:
    menor = parsernum2
if parsernum3 < menor:
    menor = parsernum3

print(f'O maior valor digitado foi {maior:.2f} e o menor valor foi {menor:.2f}.')