'''
FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERECTIVE HELP DO PYTHON. O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER.
QUANDO O USUÁRIO DIGITAR A PALAVRA 'FIM', O PROGRAMA SE ENCERRARÁ.
OBS.: USE CORES.
'''
from time import sleep

c = (
    '\033[m',               # 0- sem cor
    '\033[0;30;41m',        # 1- cor vermelha
    '\033[0;30;42m',        # 2- cor verde
    '\033[0;30;43m',        # 3- cor amarela
    '\033[0;30;44m',        # 4- cor azul
    '\033[0;30;45m',        # 5- cor roxa
    '\033[7;30m'            # 6- branca
);


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('ATÉ LOGO!', 1)
