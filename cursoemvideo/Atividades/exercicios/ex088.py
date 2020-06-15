'''
FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS
E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA. COLOCANDO OS VALORES EM ORDEM
CRESCENTE.
'''
from random import randint
from time import sleep

lista = list()
jogos = list()
print('-*-' * 30)
print('     JOGO DA MEGA SENA     ')
quant = int(input('Quantos jogos você deseja? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-*' * 3, f' SORTEANDO {quant} JOGOS ', '-*' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-*' * 5, '< BOA SORTE! >', '-*' * 5)
