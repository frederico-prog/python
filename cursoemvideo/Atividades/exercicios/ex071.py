'''
CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER
SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.
OBS.: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50, R$20, R$10 E R$1.
'''
from time import sleep
print('-=-' * 17)
print('{:^50}'.format(' CAIXA ELETRÔNICO - BANCO PYTHON '))
print('-=-' * 17)

saldo = 5879.98
saldoatual = 0
limite = 2000
while True:
    saque = int(input('Informe o valor que deseja sacar [10 - 2000]: R$ '))

    resp = ' '

    if saque > limite:
        print('O valor solicitado excede o valor máximo para saque diário.')
    if saque > saldo:
        print('O seu saldo inferior ao valor solicitado:')
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
