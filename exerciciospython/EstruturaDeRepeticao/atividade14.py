'''
14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.
'''
numeros = 10
count_par = 0
count_impar = 0
lista = []
lista_par = []
lista_impar = []

for num in range(1, numeros + 1):
    valor = int(input(f'Insira o {num}º: '))

    if valor % 2 == 0:
        lista_par.append(valor)
        count_par += 1
    else:
        lista_impar.append(valor)
        count_impar += 1

    lista.append(valor)

soma_numeros_pares = sum(lista_par)
soma_numeros_impares = sum(lista_impar)

print(f'Números: {lista}')
print(f'Números pares: {lista_par} no total de {count_par} números. A soma dos números pares é {soma_numeros_pares}.')
print(f'Números pares: {lista_impar} no total de {count_impar} números. A soma dos números impares é {soma_numeros_impares}.')
