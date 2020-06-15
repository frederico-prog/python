'''
4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

count = 0
soma = 0
for i in range(1, 5):
    nota = str(input(f'Insira a {i}ª nota do aluno. ')).replace(',', '.')
    parsernota = float(nota)
    soma += parsernota
    count += 1
media = soma / count
print(f'A média das notas é: {media}')
