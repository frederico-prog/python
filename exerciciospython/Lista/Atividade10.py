'''
10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''
import random

vetor1 = []
vetor2 = []
vetor3 = []

# Preenche a primeira lista com valores aleatórios
for n in range(0, 10):
    num = random.randint(1, 100)
    vetor1.append(num)
print(f'PRIMEIRO VETOR: {vetor1}')

# Preenche a primeira lista com valores aleatórios
for i in range(0, 10):
    num2 = random.randint(1, 100)
    vetor2.append(num2)
print(f'SEGUNDO VETOR: {vetor2}')

# Intercala os dois vetores
for a, b in zip(vetor1, vetor2):
    vetor3.append(a)
    vetor3.append(b)

# Ordena os números do vertor em ordem crescente
vetor3.sort()
print(f'VETORES 1 E 2 INTERCALADOS: {vetor3}\nTAMANHO DO VETOR: {len(vetor3)}')
