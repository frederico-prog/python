'''
Melhore o jogo do desafio 028 onde o computador vai 'pensar' um nº entre 0 e 10. Só que agora o jogador vai tentar
advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
print('-=-' * 12)
print('{:^35}'.format(' JOGO DA ADIVINHAÇÃO '))
print('-=-' * 12)

from random import randint

computador = randint(0, 4)           # FAZ O COMPUTADOR "PENSAR"

print('-=-' * 20)
print('Tente adivinhar o número que pensei...')
print('-=-' * 20)

'''
jogador1 = int(input('Em que número eu pensei? '))
count = 1
jogada = []
while jogador1 != computador:
    count += 1
    jogada.append(jogador1)
    print('Você erro! Vamos tentar mais uma vez.')
    jogador1 = int(input('Em que número eu pense? '))
print('Você precisou de {} jogadas para acertar.'.format(count))
for jogador1 in jogada:
    print('Os números jogados foram: {}'.format(jogada))
'''


from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Tente adivinhar!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
