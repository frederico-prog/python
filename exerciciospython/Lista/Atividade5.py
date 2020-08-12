'''
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
'''
lista_num = []
lista_par = []
lista_impar = []
for i in range(0, 20):
    num = int(input('Informe o número: '))
    lista_num.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f'A lista de números digitados foi: {lista_num}')
print(f'A lista de números pares digitados foi: {lista_par}')
print(f'A lista de números ímpares digitados foi: {lista_impar}')
