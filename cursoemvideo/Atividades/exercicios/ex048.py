'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e se encontram entre no
intervalo de 1 até 500
'''
print('-=-' * 20)
print('{:^60}'.format(' SOMA DE NÚMEROS ÍMPARES MÚLTIPLOS DE 3  '))
print('-=-' * 20)

s = 0
c = 0
for count in range(1, 501, 2):
    if count % 3 == 0:   # verifica se o número é divisível por 3
        c += 1
        s += count
print('A soma de todos os {} resultou na soma {}.'.format(c, s))
