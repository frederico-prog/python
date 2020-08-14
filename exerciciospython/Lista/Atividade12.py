'''
12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.
'''
import random

lista_aluno = []
soma_altura = media_altura = total_alunos = 0

for c in range(0, 30):
    aluno = []
    idade = random.randint(0, 90)
    altura = random.uniform(1.25, 2.85)
    aluno.append(idade)
    aluno.append(altura)
    lista_aluno.append(aluno)

for a in lista_aluno:
    soma_altura += a[1]

media_altura = soma_altura / len(lista_aluno)
print(f'MÉDIA DAS ALTURAS: {media_altura:.2f}m')

for aluno in lista_aluno:
    if aluno[0] >= 13 and aluno[1] < media_altura:
        total_alunos += 1

print(f'O total de alunos superior a 13 anos e com a altura inferior a {media_altura:.2f}m foi de: {total_alunos}')
