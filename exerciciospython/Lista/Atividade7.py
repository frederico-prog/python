'''
7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''
lista_num = []
mult = 1

for n in range(0, 5):
    num = int(input(f'Informe o {n + 1}º número: '))
    lista_num.append(num)
    mult = mult * num

soma = sum(lista_num)
print(f'Os números digitados foram: {lista_num}')
print(f'A soma dos números é: {soma}')
print(f'O produto dos números digitados é: {mult}')

