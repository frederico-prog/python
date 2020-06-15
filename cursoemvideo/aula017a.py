'''
Variáveis compostas
- Tuplas - não são imutáveis ()
- Listas [Parte 1] - podem ser mutáveis []
'''
#Tupla - num = (2, 5, 9, 1)
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.insert(2, 2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
num.pop()
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


valor = []
for cont in range(0, 5):
    valor.append(int(input('Digite um valor')))

a = [2, 3, 4, 7]
b = a        # cria uma ligação entre listas
b = a[:]     # copia de uma lista para outra variável
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
