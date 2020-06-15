'''
LAÇOS DE REPETIÇÃO (PARTE 1) - FOR
'''
# Ordem decrescente
for c in range(6, 0, -1):
    print(c)
print('FIM')

# contagem de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM')

# contagem de 3 em 3
for c in range(0, 7, 3):
    print(c)
print('FIM')

#
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um número: '))
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma foi {}.'.format(s))
