'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEGUÊNCIA.
NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.
'''
print('-=-' * 20)
print('{:^60}'.format(' TABELA DE PREÇOS '))
print('-=-' * 20)

produto = ('Lápis', 1.75,
           'Borracha', 2,
           'Caderno', 15.90,
           'Estojo', 25,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Caneta', 22.30,
           'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<30}', end='')
    else:
        print(f'R${produto[pos]:>7.2f}')
print('-' * 40)