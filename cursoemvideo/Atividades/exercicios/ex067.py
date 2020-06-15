'''
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO. O
PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.
'''
print('-=-' * 12)
print('{:^35}'.format(' TABUADA - v3.0 '))
print('-=-' * 12)

'''
produto = 0
resp = 'S'
while True:
    multiplicando = int(input('Digite um número: '))

    if resp in 'Ss':
        print('-' * 18)
        for multiplicador in range(1, 11):
            produto = multiplicando * multiplicador
            print(f'{multiplicando:>3} X {multiplicador:2} = {produto:2}')
        print('-' * 18)
    else:
        sair = int(input('Digite um valor negativo para sair: '))
        if sair < 0:
            break
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
print('----- FIM DA EXECUÇÃO -----')
'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
