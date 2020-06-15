'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
nome = str(input('Digite o nome desejado: ')).strip()
print('Analizando...')
print('No nome "{}" tem a palavra "SILVA"'.format(nome.upper(), nome.upper().find('SILVA')))
