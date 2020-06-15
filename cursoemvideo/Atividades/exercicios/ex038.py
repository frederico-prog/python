'''
Escreva um programa que leia dois números e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é o maior.
- O segundo valor é o maior.
- Não existe nenhum valor, os dois são iguais.
'''
# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }

print('{}****** SISTEMA DE COMPARAÇÃO ******{}'.format(cores['amarelo'], cores['limpa']))

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))

if n1 < n2:
    print('O número {} é maior que o número {}.'.format(n2, n1))
elif n1 > n2:
    print('O número {} é maior que o número {}.'.format(n1, n2))
else:
    print('Os números são iguais!')

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
