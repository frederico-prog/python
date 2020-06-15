'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
print('-=-' * 12)
print('{:^35}'.format(' SISTEMA DE CÁLCULO '))
print('-=-' * 12)

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))

menu = 0

while menu != 5:
    menu = int(
        input('Digite a opção desejada: \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair \n'))
    if menu == 1:                        # SOMAR
        soma = n1 + n2
        print('A soma entre os números {} + {} é igual a {}.'.format(n1, n2, soma))
    if menu == 2:                        # MULTIPLICAR
        mulplicacao = n1 * n2
        print('A mulplicação entre os números {} * {} é igual a {}.'.format(n1, n2, mulplicacao))
    if menu == 3:                        # MAIOR
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} foi o {}.'.format(n1, n2, maior))
    if menu == 4:                        # TROCAR OS VALORES
        n1 = float(input('Digite o novo valor para o primeiro número: '))
        n2 = float(input('Digite o novo valor para o segundo número: '))
    if menu > 5:
        print('Opção inexistente! Tente novamente.')
    sleep(2)
print('Finalizando.....')
sleep(2)
print('Obrigado por usar o nosso sistema!')
