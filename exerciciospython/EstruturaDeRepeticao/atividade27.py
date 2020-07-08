'''
27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''
turmas = int(input('Quantas turmas? '))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print('turma ', turma)
    alunos = int(input('Alunos da turma : '))
    while alunos > 40:
        print(f'turma {turma} [uma turma só pode ter 40 alunos]')
        alunos = int(input('Alunos da turma : '))
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print(f'A media é igual a: {media}')
