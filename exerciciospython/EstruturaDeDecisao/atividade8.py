'''
8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato
'''
preco1 = str(input('Insira o preço do primeiro produto: ')).replace(',', '.')
preco2 = str(input('Insira o preço do segundo produto: ')).replace(',', '.')
preco3 = str(input('Insira o preço do terceiro produto: ')).replace(',', '.')

parserpreco1 = float(preco1)
parserpreco2 = float(preco2)
parserpreco3 = float(preco3)

menor = parserpreco1

if parserpreco2 < menor:
    menor = parserpreco2
elif parserpreco3 < menor:
    menor = parserpreco3

print(f'O produto que você deve comprar é o com o valor de R$ {menor:.2f}.')
