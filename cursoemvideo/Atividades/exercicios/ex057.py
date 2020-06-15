'''
Faça um programa que leia o sexo de uma pessoa, mais só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter o valor correto.
'''
print('-=-' * 12)
print('{:^35}'.format(' SISTEMA DE VALIDAÇÃO DE DADOS '))
print('-=-' * 12)

sexo = str(input('Insira o gênero do usuário. [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Insira o gênero do usuário corretamente. [M/F]: ')).strip().upper()
print('Gênero {} registrado!'.format(sexo))
