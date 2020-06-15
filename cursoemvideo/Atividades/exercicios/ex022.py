'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maíusculas
O nome com todos as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
'''
nome = str(input('Digite o seu nome completo: ')).strip()
dividido = nome.split()
espaco = nome.count(' ')
print('Analisando...')
print('Nome com todas as letras em maiúscula {}.'.format(nome.upper()))
print('Nome com todas as letras em minúscula {}.'.format(nome.lower()))
print('Total de letras sem os espaços {}.'.format(len(nome) - espaco))
print('O primeiro nome é "{}" e contém o total de {} letras.'.format(dividido[0].upper(), len(dividido[0])))
