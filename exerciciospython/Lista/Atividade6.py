'''
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''
lista_nota = []
media_aluno = 0

# inseri as notas dos alunos
for a in range(0, 10):
    lista_nota_aluno = []
    for n in range(0, 4):
        nota_str = str(input(f'Informe a {n + 1}ª nota do {a + 1}º aluno: ')).replace(',', '.')
        nota = float(nota_str)
        lista_nota_aluno.append(nota)
    lista_nota.append(lista_nota_aluno)

# verifica a media de alunos acima de 7 ptos
for nota_aluno in lista_nota:
    soma_nota = 0
    for nota in nota_aluno:
        soma_nota += nota
    media = soma_nota / 4
    if media >= 7:
        media_aluno += 1

# imprimi o resultado na tela conforme resultado da média de alunos
if media_aluno == 0:
    print(f'Não houveram alunos com média igual ou superior a 7.0 ptos.')
else:
    print(f'A média de alunos acima de 7 ptos foi de: {media_aluno}')
