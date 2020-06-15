''''
minha_lista = []    # LISTA (list)
minha_tupla = ()    # TUPLA (tuple)
meu_dicionario = {'key': 'value'}     # DICIONÁRIO (dict)
meu_conjunto = {}   # CONJUNTO (set)
'''

# minha_tupla = ('Gui', 'João')
#
# if 'Gui' in minha_tupla:
#     print('Nome se encontra na coleção.')
#
# for nome in minha_tupla:
#     print(nome)

# meu_dicionario = {'nome': 'Frederico', 'idade': 41}
# meu_dicionario['endereco'] = 'Av. Brasilia'
# meu_dicionario['telefone'] = 31989805397
# print(meu_dicionario['idade'])
#
# if 'Frederico' in meu_dicionario.values():
#     print('Nome incluido na coleção')
#
# for valor in meu_dicionario.values():
#     print(valor)
#
# print(len(meu_dicionario))

# meu_conjunto = {'Gui', 'Joao'}
# meu_conjunto.add('Maria')
# meu_conjunto.add('Gui')
# print(meu_conjunto)
# print(len(meu_conjunto))
#
# if 'Gui' in meu_conjunto:
#     print('Foi encontrado dentro do conjunto')

# lista = list()
# conjunto = {'Frederico', 'Daisy'}
# lista.append(conjunto)
# print(lista)

conj_num_naturais = set()
conj_num_inteiros = set()

for num in range(-10, 11):
    conj_num_inteiros.add(num)

for num in range(0, 11):
    conj_num_naturais.add(num)


print('Números inteiros: ', conj_num_inteiros)
print('Números reais: ', conj_num_naturais)
uniao = conj_num_inteiros.union(conj_num_naturais)
intesercao = conj_num_inteiros.intersection(conj_num_naturais)
diferenca = conj_num_inteiros.difference(conj_num_naturais)
print('União: ', uniao)
print('Intesercao: ', intesercao)
print('Diferenca: ', diferenca)