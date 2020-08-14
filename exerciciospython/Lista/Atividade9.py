'''
9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
do vetor.
'''
from math import pow

vetor = []
soma = 0

for v in range(0, 10):
    num = int(input(f'Informe o {v + 1}º número: '))
    dobro = pow(num, 2)
    vetor.append(dobro)

# Imprime os valos digitados
print(f'Vetor de números digitados: {vetor}')

# Realiza a soma de todos os resultados do vetor e o imprime
soma = sum(vetor)
print(f'A soma dos números do vetor foi de: {soma}')
