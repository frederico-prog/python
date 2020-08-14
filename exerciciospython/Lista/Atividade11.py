'''
11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''
import random

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

# Preenche a primeira lista com valores aleatórios
for n in range(0, 10):
    num = random.randint(1, 100)
    vetor1.append(num)
print(f'PRIMEIRO VETOR: {vetor1}')

# Preenche a segunda lista com valores aleatórios
for i in range(0, 10):
    num2 = random.randint(1, 100)
    vetor2.append(num2)
print(f'SEGUNDO VETOR: {vetor2}')

# Preenche a terceira lista com valores aleatórios
for i in range(0, 10):
    num3 = random.randint(1, 100)
    vetor3.append(num3)
print(f'TERCEIRO VETOR: {vetor3}')

# Intercala os dois vetores
for a, b, c in zip(vetor1, vetor2, vetor3):
    vetor4.append(a)
    vetor4.append(b)
    vetor4.append(c)

# Ordena os números do vertor em ordem crescente
vetor4.sort()
print(f'VETORES 1, 2 E 3 INTERCALADOS: {vetor4}\nTAMANHO DO VETOR: {len(vetor4)}')
