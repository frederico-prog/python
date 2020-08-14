'''
14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a - "Telefonou para a vítima?"
    b - "Esteve no local do crime?"
    c - "Mora perto da vítima?"
    d - "Devia para a vítima?"
    e - "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''
lista_resposta = []
count_sim = 0
# count_nao = 0

print('RESPONDA APENAS "SIM" OU "NÃO"')
pergunta1 = str(input('Telefonou para a vítima?')).upper()
pergunta2 = str(input('Esteve no local do crime?')).upper()
pergunta3 = str(input('Mora perto da vítima?')).upper()
pergunta4 = str(input('Devia para a vítima?')).upper()
pergunta5 = str(input('Já trabalhou com a vítima?')).upper()

# Insere as respotas na lista
lista_resposta.append(pergunta1)
lista_resposta.append(pergunta2)
lista_resposta.append(pergunta3)
lista_resposta.append(pergunta4)
lista_resposta.append(pergunta5)

# Verifica a quantidade de respostas
for questao in lista_resposta:
    if questao == 'SIM':
        count_sim += 1
    # else:
    #     count_nao += 1

# Classifica o(a) suspeito(a) em SUSPEITA, CÚMPLICE, ASSASINO e INOCENTE
if count_sim != 0:
    if count_sim <= 2:
        print('SUSPEITO(A)')
    elif count_sim == 3 or count_sim <= 4:
        print('CÚMPLICE')
    elif count_sim == 5:
        print('ASSASSINO(A)')
else:
    print('INOCENTE')

