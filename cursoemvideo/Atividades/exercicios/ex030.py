'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''
print('***** PAR OU ÍMPAR *****')
n1 = int(input('Digite um número: '))
if n1 % 2 == 0:
    print('O número {} é PAR!!'.format(n1))
else:
    print('O número {} é ÍMPAR!!'.format(n1))
print('Tente novamente!')
