'''
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
print('Insira 5 números:')
lista = []
qtde = 0

for i in range(1, 6):
    num = int(input(f'Informe o {i}º número: '))
    lista.append(num)
    qtde += 1

soma_numeros = sum(lista)
media = soma_numeros / qtde

print(f'Números digitados: {lista}')
print(f'Soma: {soma_numeros}')
print(f'Média: {media}')
