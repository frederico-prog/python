'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randrange
from time import sleep
print('***** JOGO DE ADIVINHAÇÃO *****')
num = int(input('Digite um número de 0 a 5. '))
print('PROCESSANDO...')
sleep(3)
numpensado = randrange(5)
if num == numpensado:
    print('O número {} digitado corresponde ao número {} pensado por mim. PARABÉNS!!'.format(num, numpensado))
else:
    print('O número {} digitado não corresponde ao número {} pensado por mim.'.format(num, numpensado))
print('Tente novamente!!')


'''
from random import randint
from time import sleep
computador = randint(0, 5) # FAZ O COMPUTADOR "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉSN! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador)
'''
