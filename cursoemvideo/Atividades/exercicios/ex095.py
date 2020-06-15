'''
APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DE
APROVEITAMENTO DE CADA JOGADOR.
'''
jogador = dict()
partida = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).upper()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0, total):
        partida.append(int(input(f' Quantos gols na partida {c + 1}ª? ')))
    jogador['gol'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostar dado de qual jogador? Digite 999 para parar: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gol']):
            print(f'  No jogo {i + 1} fez {g} gols.')
    print('-=' * 40)
print('VOLTE SEMPRE!!')

