'''
21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
    a- Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
    5 e uma nota de 1;
    b- Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
    de 10, uma nota de 5 e quatro notas de 1.
'''
from time import sleep

print('-=-' * 17)
print('{:^50}'.format(' CAIXA ELETRÔNICO - BANCO PYTHON '))
print('-=-' * 17)

saldo = 5879.98
saldoatual = 0
limitemaximo = 600
limiteminimo = 10

while True:
    saque = int(input('Informe o valor que deseja sacar [10 - 600]: R$ '))

    resp = ' '

    if (saque > limitemaximo) or (saque < limiteminimo):
        print('O valor solicitado deve ser no mínimo R$ 10.00 e o valor máximo de R$ 600.00.')
        break
    if saque > saldo:
        print('O seu saldo inferior ao valor solicitado:')
        break
    else:
        saldoatual = saldo - saque
        print(f'Seu saldo atual é de R$ {saldoatual:.2f}.')
        print('Contando as notas.')

        sleep(5)

        cem = int(saque / 100)
        saque = saque - (cem * 100)

        cinquenta = int(saque / 50)
        saque = saque - (cinquenta * 50)

        vinte = int(saque / 20)
        saque = saque - (vinte * 20)

        dez = int(saque / 10)
        saque = saque - (dez * 10)

        cinco = int(saque / 5)
        saque = saque - (cinco * 5)

        um = saque

        sleep(2)

        if cem > 0:
            print(f'Notas de R$100,00 - {cem}')
        if cinquenta > 0:
            print(f'Notas de R$50,00 - {cinquenta}')
        if vinte > 0:
            print(f'Notas de R$20,00 - {vinte}')
        if dez > 0:
            print(f'Notas de R$10,00 - {dez}')
        if cinco > 0:
            print(f'Notas de R$5,00 - {cinco}')
        if um > 0:
            print(f'Notas de R$1,00 - {um}')

        print('Favor retirar o dinheiro no local indicado.')

        while resp not in 'SC':
            resp = str(input('Pressione "S" para sair ou "C" para continuar.')).strip().upper()[0]
        if resp == 'S':
            break

print('VOLTE SEMPRE!')
