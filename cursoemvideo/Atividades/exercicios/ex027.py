'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
n = str(input('Digite o nome desejado: ')).strip().upper()
nome = n.split()
print('É um prazer te conhecer!')
print('O seu primeiro nome é: {}.'.format(nome[0]))
print('O seu último nome é: {}.'.format(nome[len(nome) - 1]))
