'''
1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
lista_num = []
for num in range(1, 6):
    valor = int(input(f'Informe o {num}: '))
    lista_num.append(valor)
print(lista_num)
