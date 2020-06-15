'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIM E PASSO E REALIZE A
CONTAGEM.
SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
A- DE 1 ATÉ 10, DE 1 EM 1
B- DE 10 ATÉ 0, DE 2 EM 2
C- UMA CONTAGEM PERSONALIZADA.
'''
from time import sleep


def titulo(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'{  txt}')
    print('-' * tam)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {i} a {f} de {p} em {p}.')
    sleep(1.5)

    if i < f:
        for n in range(i, f + 1, p):
            print(f'{n}', end=' ', flush=True)
            sleep(0.5)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
    print('FIM')


# PROGRAMA PRINCIPAL
titulo('SISTEMA DE CONTADOR')

contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 20)
print('Sua vez de personalizar a contagem!')
inicio = int(input('Início:  '))
fim = int(input('Fim:     '))
passo = int(input('Passo:   '))
contador(inicio, fim, passo)
