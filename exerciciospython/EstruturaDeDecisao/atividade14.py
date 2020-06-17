'''
14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
n1 = str(input('Informe a primeira nota: ')).replace(',', '.')
n2 = str(input('Informe a segunda nota: ')).replace(',', '.')

nota1 = float(n1)
nota2 = float(n2)

media = (nota1 + nota2) / 2

if 9 < media >= 10:
    print(f'Primeira nota:\t\t{nota1:.2f}')
    print(f'Segunda nota:\t\t{nota2:.2f}')
    print(f'Média das notas:\t{media:.2f}')
    print(f'Conceito:\t\t\tA')
    print(f'Situação:\t\t\tAprovado')
elif 7.5 < media <= 9:
    print(f'Primeira nota:\t\t{nota1:.2f}')
    print(f'Segunda nota:\t\t{nota2:.2f}')
    print(f'Média das notas:\t{media:.2f}')
    print(f'Conceito:\t\t\tB')
    print(f'Situação:\t\t\tAprovado')
elif 6 < media >= 7.5:
    print(f'Primeira nota:\t\t{nota1:.2f}')
    print(f'Segunda nota:\t\t{nota2:.2f}')
    print(f'Média das notas:\t{media:.2f}')
    print(f'Conceito:\t\t\tC')
    print(f'Situação:\t\t\tAprovado')
elif 4 < media >= 6:
    print(f'Primeira nota:\t\t{nota1:.2f}')
    print(f'Segunda nota:\t\t{nota2:.2f}')
    print(f'Média das notas:\t{media:.2f}')
    print(f'Conceito:\t\t\tD')
    print(f'Situação:\t\t\tReprovado')
elif 0 < media >= 4:
    print(f'Primeira nota:\t\t{nota1:.2f}')
    print(f'Segunda nota:\t\t{nota2:.2f}')
    print(f'Média das notas:\t{media:.2f}')
    print(f'Conceito:\t\t\tE')
    print(f'Situação:\t\t\tReprovado')
