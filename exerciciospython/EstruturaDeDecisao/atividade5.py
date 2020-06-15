'''
5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
    a- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    b- A mensagem "Reprovado", se a média for menor do que sete;
    c- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota1 = str(input('Insira a primeira nota: ')).replace(',', '.')
nota2 = str(input('Insira a segunda nota: ')).replace(',', '.')

parsernota1 = float(nota1)
parsernota2 = float(nota2)

media = (parsernota1 + parsernota2) / 2

if 7 <= media < 10:
    print('Aluno aprovado.')
elif media < 7:
    print('Aluno reprovado.')
elif media == 10:
    print('Aluno aprovado com distinção')
else:
    print('Dados digitados incorretos.')
