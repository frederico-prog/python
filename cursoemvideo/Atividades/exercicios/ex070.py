'''
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO
FINAL, MOSTRE:
A- QUAL É O TOTAL GASTO NA COMPRA
B- QUANTOS PRODUTOS CUSTAM MAIS DE R$1000.
C- QUAL É O NOME DO PRODUTO MAIS BARATO.
'''
print('-=-' * 17)
print('{:^50}'.format(' LOJA DE PYTHON '))
print('-=-' * 17)
print('{:-^50}'.format(' ANALISE DE DADOS DE VENDAS '))

totalcompra = count = menor = maior = c = 0
lista = []

while True:
    c += 1
    produto = str(input('Insira o nome do produto: ')).strip().upper()
    preco = float(input(f'Insira o preço do produto {produto}: R$ '))

    totalcompra += preco
    tipo = ' '
    produtomenor = ' '
    if c == 1 or preco < menor:
        menor = preco
        produtomenor = produto
    '''else:
        if preco < menor:
            menor = preco
            produtomenor = produto'''
    if preco >= 1000:
        count += 1
        lista.append(produto)
    while tipo not in 'CS':
        tipo = str(input('Deseja continuar? "C" para continuar "S" para sair.')).strip().upper()[0]
    if tipo == 'S':
        break

print(f'Total da compra: R${totalcompra:.2f}'
      f'\nTotal de produtos acima de R$ 1.000: {count}'
      f'\nLista dos produtos acima de R$ 1.000: {lista}'
      f'\nO menor valor é o do produto {produtomenor} com o custo de R${menor:.2f}.')
print('VOLTE SEMPRE!!!!')
