'''
20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e presentar:
    a- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c- A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
n1 = str(input('Insira a primeira nota: ')).strip().replace(',', '.')
n2 = str(input('Insira a segunda nota: ')).strip().replace(',', '.')
n3 = str(input('Insira a terceira nota: ')).strip().replace(',', '.')

nota1 = float(n1)
nota2 = float(n2)
nota3 = float(n3)


somanota = (nota1 + nota2 + nota3)
media = somanota / 3

if media >= 10:
    print(f'Total nota: {somanota:.2f}\nSituação: Aprovado com distinção.')
elif 7 <= media < 10:
    print(f'Total nota: {somanota:.2f}\nMédia: {media:.2f}\nSituação: Aprovado.')
else:
    print(f'Total nota: {somanota:.2f}\nMédia: {media:.2f}\nSituação: Reprovado.')
