'''
7 - Faça um programa que leia 5 números e informe o maior número.
'''
print('Insira 5 números:')
lista = []

for i in range(1, 6):
    num = int(input(f'Informe o {i}º número: '))
    lista.append(num)

print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')