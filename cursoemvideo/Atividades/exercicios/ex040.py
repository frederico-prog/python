'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou ou superior: APROVADO(A)
'''
from time import sleep

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }

print('{}****** SISTEMAS DE NOTAS ******{}'.format(cores['amarelo'], cores['limpa']))

aluno = str(input('Nome do aluno: ')).strip().upper()

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 5:
    print('O(a) aluno(a) {} foi reprovado(a)! Sua média foi {:.2f}.'.format(aluno, media))
elif 5 < media > 6.9:
    print('O(a) aluno(a) {} ficou de recuperação! Sua média foi {:.2f}.'.format(aluno, media))
else:
    print('O(a) aluno(a) {} foi aprovado(a)! Sua média foi {:.2f}.'.format(aluno, media))

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
