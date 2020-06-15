'''
FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO
O TOTAL DE VITÓRIAS CONSECULTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
'''
from random import randint

print('-=-' * 12)
print('{:^35}'.format(' JOGO DO PAR OU ÍMPAR '))
print('-=-' * 12)

v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. O total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
        print('Vamos jogar novamente!')
print(f'GAME OVER! Você venceu {v} vezes.')
