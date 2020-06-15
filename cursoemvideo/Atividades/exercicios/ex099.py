'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.
'''
from time import sleep
from random import randint

def quebralin():
    print('-=' * 20)


def numaleatorio():
    tamanho = randint(0, 10)
    cont = 0
    numero = list()
    while cont < tamanho:
        numero.append(randint(0, 100))
        cont += 1
    maior(numero)
    #print(tamanho, numero)


def maior(lst):
    cont = maiornum = pos = 0
    print(lst)
    quebralin()
    print('Analisando os valores passados...')
    for valor in lst:
        print(f'{valor} ', end=' ', flush=True)
        sleep(0.4)
        if valor == 0:
            maiornum = valor
        else:
            if valor > maiornum:
                maiornum = valor
    print(f'\nAo todo foram informados {len(lst)} valores.')
    print(f'O maior valor informado foi o número {maiornum}.')


numaleatorio()
