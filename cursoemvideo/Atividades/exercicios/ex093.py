'''
CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS
PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ QUARDADO EM UM
DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.
'''
jogador = dict()
partida = list()
jogador['nome'] = str(input('Nome do jogador: ')).upper()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partida.append(int(input(f' Quantos gols na partida {c + 1}ª? ')))
jogador['gol'] = partida[:]
jogador['total'] = sum(partida)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} realizou {len(jogador["gol"])} partidas.')
for i, v in enumerate(jogador['gol']):
    print(f'     => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
