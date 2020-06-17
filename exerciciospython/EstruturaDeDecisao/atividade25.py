'''
25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a- "Telefonou para a vítima?"
    b- "Esteve no local do crime?"
    c- "Mora perto da vítima?"
    d- "Devia para a vítima?"
    e- "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''
import time

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'cinza': '\033[37m',
         'vermelhoescuro': '\033[91m',
         'verde': '\033[32m',
         'azul': '\033[34m'
         }

print('{}****** SISTEMA DE INVESTIGAÇÃO ******{}'.format(cores['amarelo'], cores['limpa']))
print('{}QUESTIONÁRIO{}'.center(40).format(cores['azul'], cores['limpa']))

print('Responda "SIM" ou "NÂO" para as questões a seguir.')
p1 = str(input('Telefonou para a vitíma? ')).upper().strip()
p2 = str(input('Esteve no local do crime? ')).upper().strip()
p3 = str(input('Mora perto da vitíma? ')).upper().strip()
p4 = str(input('Devia para a vitíma? ')).upper().strip()
p5 = str(input('Já trabalhou com a vitíma? ')).upper().strip()

resposta = []

# Atribui um valor para cada tipo de resposta. "SIM" recebe 1 - "NÃO" recebe 0
if p1 == 'SIM':
    count = 1
    resposta.append(count)
else:
    count = 0
    resposta.append(count)

if p2 == 'SIM':
    count = 1
    resposta.append(count)
else:
    count = 0
    resposta.append(count)

if p3 == 'SIM':
    count = 1
    resposta.append(count)
else:
    count = 0
    resposta.append(count)

if p4 == 'SIM':
    count = 1
    resposta.append(count)
else:
    count = 0
    resposta.append(count)

if p5 == 'SIM':
    count = 1
    resposta.append(count)
else:
    count = 0
    resposta.append(count)

# Realiza a contagem das respostas "SIM" e "NÂO"
numrespostasim = 0
numrespostanao = 0

for i in resposta:
    if i == 1:
        numrespostasim += 1
    else:
        numrespostanao += 1

# Identifca se o intrevistado é Inocente, Cúmplice, Suspeito ou Assassino
print('Analisando as respostas...')
time.sleep(1)
if numrespostasim == 0:
    print(f'{cores["verde"]}INOCENTE!{cores["limpa"]}')
    print(f'Número de respostas "SIM": {numrespostasim}\nNúmero de respostas "NÃO": {numrespostanao}')
elif numrespostasim == 2:
    print(f'{cores["azul"]}SUSPEITO!{cores["limpa"]}')
    print(f'Número de respostas "SIM": {numrespostasim}\nNúmero de respostas "NÃO": {numrespostanao}')
elif 2 < numrespostasim <= 4:
    print(f'{cores["cinza"]}CÚMPLICE!{cores["limpa"]}')
    print(f'Número de respostas "SIM": {numrespostasim}\nNúmero de respostas "NÃO": {numrespostanao}')
else:
    print(f'{cores["vermelhoescuro"]}ASSASSINO!{cores["limpa"]}')
    print(f'Número de respostas "SIM": {numrespostasim}\nNúmero de respostas "NÃO": {numrespostanao}')

print('FIM DA EXECUÇÃO DO PROGRAMA')
