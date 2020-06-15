'''
A Confederação Nacional de Natação precisa de um sistema que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a sua idade:
- Até 9 anos: MIRIMM
- Até 15 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER
'''
from time import sleep
from datetime import date

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }

print('{}****** SISTEMA DE MATRÍCULA ******{}'.format(cores['amarelo'], cores['limpa']))

aluno = str(input('Nome do candidato: ')).strip().upper()
ano = int(input('Ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - ano
idademinima = 5

print('VERIFICANDO A CATEGORIA PARA O ALUNO {}'.format(aluno))
sleep(3)

if idademinima < idade < 9:
    print('A categoria do aluno {} é a MIRIM.'.format(aluno))
elif 9.5 < idade < 15:
    print('A categoria do aluno {} é a INFANTIL.'.format(aluno))
elif 15.5 < idade < 19:
    print('A categoria do aluno {} é a JUNIOR.'.format(aluno))
elif 19.5 < idade < 20:
    print('A categoria do aluno {} é a SÊNIOR.'.format(aluno))
elif idade > 20.5:
    print('A categoria do aluno {} é a MASTER.'.format(aluno))
else:
    print('O aluno {} ainda não atingiu a idade mínima de {} para se inscrever nas aulas.'.format(aluno, idademinima))

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
