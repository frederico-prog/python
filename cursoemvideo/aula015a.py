'''
LAÇOS DE REPETIÇÃO (PARTE 3) - WHILE(break)
'''
'''
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('ACABOU!')
'''

'''
n = count = s = 0
while n != 999:
    n = int(input('Digite um nº: '))
    s += n
    count += 1
print('Soma {} \nQtde: {}'.format(s, count))
'''

n = count = s = 0
while True:
    n = int(input('Digite um nº: '))
    if n == 999:
        break
    s += n
    count += 1
#print('Soma {} \nQtde: {}'.format(s, count))
print(f'Soma {s} \nQtde: {count}')

