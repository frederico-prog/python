'''
Crie um programa que faça o computador jogar Jokenpô com você
'''
from random import randint
from time import sleep

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }
print('-=-' * 20)
print('{}****** JOGO DO JOKENPÔ ******{}'.format(cores['amarelo'], cores['limpa']))

jogador = int(input('Escolha entre: \n- 0 para PEDRA \n- 1 para PAPEL \n- 2 para TESOURA \nDigite a sua escolha: '))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)

print('JO\n')
sleep(1)
print('KEN\n')
sleep(1)
print('POOH!!!\n')
sleep(3)

print('-' * 20)
print('Jogador 1: {}'.format(lista[jogador]))
print('Computador: {}'.format(lista[computador]))
print('-' * 20)

if computador == 0:
    if jogador == 0:
        print('Não houve ganhador!!!')
    elif jogador == 1:
        print('Jogador 1 perdeu!!!')
    elif jogador == 2:
        print('Computador venceu!!!')
    else:
        print('Operação inválida!!!')
elif computador == 1:
    if jogador == 0:
        print('Computador perdeu !!!')
    elif jogador == 1:
        print('Não houve ganhador!!!')
    elif jogador == 2:
        print('Jogador 1 ganhou!!!')
    else:
        print('Operação inválida!!!')
elif computador == 2:
    if jogador == 0:
        print('Jogador 1 venceu!!!')
    elif jogador == 1:
        print('Computador venceu!!!')
    elif jogador == 2:
        print('Não houve vencedor!!!')
    else:
        print('Operação inválida!!!')
else:
    print('Operação inválida!!')

print('JOGUE NOVAMENTE!!!')
print('-=-' * 20)
