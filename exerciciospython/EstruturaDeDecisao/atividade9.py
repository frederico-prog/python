'''
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
num1 = str(input('Insira o primeiro número: ')).replace(',', '.')
num2 = str(input('Insira o segundo número: ')).replace(',', '.')
num3 = str(input('Insira o terceiro número: ')).replace(',', '.')

n1 = float(num1)
n2 = float(num2)
n3 = float(num3)

lista = [n1, n2, n3]
ordem = sorted(lista, reverse=True)

print(f'Ordem decrescente: {ordem}')
