'''
LAÇOS DE REPETIÇÃO (PARTE 2) - WHILE
'''
'''
for c in ragen(1, 10):
    print(c)
print('Fim')
'''

'''
c =1
while c < 10:
    print(c)
    c += 1
print('Fim')
'''

'''
for c in range(1, 5)
    n = int(input('Digite um valor: '))
print('Fim')
'''

'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''

'''
n = 'S'
while n == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim')
'''


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 0
print('Vc digitou {} números pares e {} ímpares!'.format(par, impar))
