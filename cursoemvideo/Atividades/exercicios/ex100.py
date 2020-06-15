'''
FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADA SORTEIO() E SOMAPAR(). A PRIMEIRA FUNÇÃO VAI
SORTEAR 5 NÚMEROS E VAI COLOCA-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES
SORTEADOS PELA FUNÇÃO ANTERIOR.
'''
from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando os números: ', end=' ')
    for cont in range(0, 5):
        num = randint(1, 10)
        lst.append(num)
        print(f'{num} ', end=' ', flush=True)
        sleep(0.3)
    somapar(lst)


def somapar(lst):
    soma = 0
    par = list()
    for valor in lst:
        if valor % 2 == 0:
            par.append(valor)
            soma += valor
    print(f'\nOs números pares foram: {par}. \nA soma entre eles foi de: {soma}.')


listanum = list()
sorteio(listanum)
