'''
Variáveis compostas
- Tuplas - são imutáveis ()
'''

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print('Ordenado: ', sorted(lanche)) # coloca a tupla em ordem
print('Desordenado: ', lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[-2:])
print(lanche[-3:])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

# Com len e com a posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# Sem o tamanho
print('Meu cardápio de hoje')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# Mostrando a posição do elemento
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {lanche[cont]} na posição {pos}')


# tuplas são imutáveis
'''lanche[1] = 'Refrigerante'''


a = (2, 5, 4)
b = (5, 8, 1, 2)
c1 = a + b
c = b + a
print(c)
print(c1)
print(c.count(5))
print(c.count(4))
print(c.count(9))
print(c.index(8))
print(c.index(4))
print(c.index(2))
print(c.index(5, 1))

# tupla aceita vários tipos de dado
pessoa = ('Gustavo', 39, 99.88)
# del(pessoa[0])
# del(pessoa)
print(pessoa)