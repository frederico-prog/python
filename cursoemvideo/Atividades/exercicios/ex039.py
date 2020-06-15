'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'
         }

print('{}****** SISTEMA DE ALISTAMENTO MILITAR ******{}'.format(cores['amarelo'], cores['limpa']))

candidato = str(input('Candidato: ')).strip().upper()
ano = int(input('Informe o seu ano de nascimento: '))
sexo = str(input('Informe o sexo do candidato: \nM para MASCULINO \nF para FEMININO \n')).strip().upper()

anoatual = date.today().year
idade = anoatual - ano
idademin = 18

if sexo == 'M':
    if idade < idademin:
        resultado = idademin - idade
        saldo = anoatual + resultado
        print('O candidato {} ainda não tem a idade mínima para se alistar.'.format(candidato))
        print('Ainda falta(m) {} ano(s) para se alistar.'.format(resultado))
        print('O seu alistamento deverá ser realizado em {}.'.format(saldo))
    elif idade == idademin:
        print('O candidato {} já tem idade necessária para se alistar.'.format(candidato))
        print('{}APROVADO!{}'.format(cores['verde'], cores['limpa']))
    else:
        resultado = idade - idademin
        saldo = anoatual - resultado
        print('O candidato {} deveria ter se alistado à {} anos atrás.'.format(candidato, resultado))
        print('{}REALIZAR O ALISTAMENTO!{}'.format(cores['vermelho'], cores['limpa']))
        print('O seu alistamento deveria ter sido feito em {}.'.format(saldo))
else:
    print('O alistamento ainda não está liberado para o sexo feminino.')

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
