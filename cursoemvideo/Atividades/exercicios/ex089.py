'''
CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM
BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE.
'''
from time import sleep

# Lista principal, recebe das outras listas
# o nome do aluno, as notas dentro de uma lista e a média.
alunos = list()
dados = list()  # Guarda o nome e a nota média do aluno temporariamente.
notas = list()  # Guarda as duas notas de cada aluno temporariamente.

while True:
    dados.append(str(input('\nNome: ').title()))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    dados.append(notas[:])
    dados.append((notas[0] + notas[1]) / 2)
    alunos.append(dados[:])
    # Limpa as listas para novos dado de novos alunos.
    dados.clear()
    notas.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar not in 'SN':
            print('Digite apenas "S" para não e "N" para não.')
    if continuar == 'N':
        break

# Mostra uma tabela com o índice, o nome e a média dos alunos.
print(f'\n{"=-=" * 10}\n{"Número:   NOME:        Média:"}')
for i, aluno in enumerate(alunos):
    print(f'{i:^7}  {aluno[0]:^7}  {aluno[2]:>9.1f}')
print(f'{"=-=" * 10}')

while True:
    # Pergunta o número do aluno de acordo com a tabela para ver as notas dele.
    prompt = '\nGostaria de mostrar as notas de qual aluno?\n'
    prompt += f'{"(999 para interromper o programa)":^43}'
    number = int(input(f'{prompt}\nNúmero: '))

    # Se o número 999 for digitado, interrompe o programa.
    if number == 999:
        print(f'\n{"=-=" * 5}\n{"FINALIZANDO..."}\n{"=-=" * 5}')
        sleep(2)
        break

    # Percorre a lista de cada aluno com o seu índice.
    for i, aluno in enumerate(alunos):
        # Verifica se o número digitado é o mesmo que o índice do aluno na lista
        # se for, mostra as notas em forma de lista e o nome do aluno.
        if number == i:
            print('=-=' * 11)
            print(f'As notas de {aluno[0]} são {aluno[1]}')
            print('=-=' * 11)


'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: ')) 
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print('-*' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":<8}')
print('-*' * 26)
for i, a in enumarete(ficha):
    print(f'{i:<4}{a[0]:<10}{a[1]:<8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe: )'
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE! >>>')
 '''