'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E
QUANTOS GOLS ELE MARCOU.
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.
'''


def ficha(name='', goal=0):
    if name != '' and goal >= 0:
        return f'O jogador {name} fez {goal} gols.'
    elif name == '' and goal >= 0:
        player = '<< desconhecido >>'
        return f'O jogador {player} fez {goal} gols.'
    else:
        player = '<< desconhecido >>'
        return f'O jogador {player} fez {goal} gols.'


# PROGRAMA PRINCIPAL
name = str(input('Informe o nome do jogador: ')).upper().strip()
goal = str(input('Informe a qtde de gols: ')).strip()
if goal.isnumeric():
    goal = int(goal)
    print(ficha(name, goal))
else:
    goal = 0
    print(ficha(name, goal))
