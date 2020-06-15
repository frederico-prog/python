'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
'''
# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'verde': '\033[4:32m'
         }

num = int(input('Informe um número: '))

print('-=-' * 12)
print('{:^35}'.format(' TABUADA  DO {}').format(num))
print('-=-' * 12)

produto = 0
soma = 0
divisor = 0
subtracao = 0

print('{}MULTIPLICAÇÃO{}'.format(cores['verde'], cores['limpa']))
for count in range(1, 11):
    produto = num * count
    print('{} * {} = {}'.format(count, num, produto))

print('{}SOMA{}'.format(cores['verde'], cores['limpa']))
for count in range(1, 11):
    soma = num + count
    print('{} + {} = {}'.format(count, num, soma))

print('{}DIVISÃO{}'.format(cores['verde'], cores['limpa']))
for count in range(1, 11):
    produto = num * count
    divisor = produto / num
    print('{:.0f} / {:.0f} = {:.0f}'.format(produto, num, divisor))

print('{}SUBTRAÇÃO{}'.format(cores['verde'], cores['limpa']))
for count in range(1, 11):
    soma = num + count
    subtracao = soma - num
    print('{:.0f} - {:.0f} = {:.0f}'.format(soma, num, subtracao))

print('***** FIM DA EXECUÇÃO *****')
