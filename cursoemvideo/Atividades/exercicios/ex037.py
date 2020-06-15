'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
from time import sleep

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }

print('{}****** SISTEMA DE CONVERSÃO ******{}'.format(cores['amarelo'], cores['limpa']))

escolha = int(input('Selecione a opção desejada: \n1-Decimal para Binário \n2-Decimal para Octal \n'
                    '3-Decimal para Hexadecimal \n'))
if escolha == 1:
    print('CONVERTE DECIMAL PARA BINÁRIO')
    n1 = int(input('Insira o número: '))
    print('CONVERTENDO O NÚMERO {}...'.format(n1))
    sleep(3)
    conversao = bin(n1)[2:]
    print('O número {} na base 2 é {}'.format(n1, conversao))
elif escolha == 2:
    print('CONVERTE DECIMAL PARA OCTADECIMAL')
    n1 = int(input('Insira o número: '))
    print('CONVERTENDO O NÚMERO {}...'.format(n1))
    sleep(3)
    conversao = oct(n1)[2:]
    print('O número {} na base 8 é {}'.format(n1, conversao))
elif escolha == 3:
    print('CONVERTE DECIMAL PARA HEXADECIMAL')
    n1 = int(input('Insira o número: '))
    print('CONVERTENDO O NÚMERO {}...'.format(n1))
    sleep(3)
    conversao = hex(n1)[2:]
    print('O número {} na base 16 é {}'.format(n1, conversao))
else:
    print('Opção selecionada não existe! Por favor, selecione uma das opções acima sitada.')

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
