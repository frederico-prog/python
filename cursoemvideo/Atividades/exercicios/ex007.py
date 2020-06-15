# Desenvolva um programa que leia as duas notas de um aluno aluno, calcule e mostre a sua média
print('******** DESAFIO - AULA 07 - MÉDIA *********')
aluno = input('Entre com o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a próxima nota: '))
media = (n1 + n2) / 2
print('A média das notas do aluno {} foi de {:.1f}'.format(aluno, media))
