'''
26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
'''
# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'cinza': '\033[37m',
         'verde': '\033[32m',
         'azul': '\033[34m'
         }

# Lista de candidados
lista_candidato = [
    [123, 'AA', 0],
    [567, 'BB', 0],
    [890, 'CC', 0]
]

# Declaração de variáveis
run = True
votante = voto = maior = 0

# Menu incial
print(' ')
print(f'{cores["azul"]}- {cores["limpa"]}' * 17, end='')
print(f'{cores["azul"]}URNA ELETRÔNICA{cores["limpa"]}'.center(20), end='')
print(f'{cores["azul"]} -{cores["limpa"]}' * 17)
print(' ')

print('Candidato AA = 123\nCandidato BB = 567\nCandidato CC = 890')

qtde_eleitor = int(input('Informe a quantidade de eleitores da zona eleitoral: '))

while votante < qtde_eleitor:

    numeroCandidato = int(input('Informe o número do seu candidato: '))

    for candidato in lista_candidato:

        if numeroCandidato == candidato[0]:
            if candidato[0] == 0:
                candidato[2] = 1
                break

            if candidato[0] > 0:
                candidato[2] += 1
                break

    votante += 1

for candidato in lista_candidato:
    print(f'O candidato {candidato[1]} teve {candidato[2]} votos.')
