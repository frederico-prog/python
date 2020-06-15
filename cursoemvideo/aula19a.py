'''
Variáveis compostas
- Tuplas - não são imutáveis ()
- Listas [Parte 2] - podem ser mutáveis [] ou list()
- Dicionários - {} permite a personalização dos índices
'''
# Declaração de dicionário
# dado = {}
# dado = dict()
#
# dado = {'nome': 'Pedro', 'idade': 25}
# print(dado['nome'])         # IMPRIME O VALOR DO CAMPO NOME
# print(dado['idade'])        # IMPRIME O VALOR DO CAMPO IDADE
# dado['sexo'] = 'M'          # CRIA UM NOVO CAMPO E ADICIONA O ELEMENTO AO DICIONARIO
# del dado['idade']           # REMOVE O INDICE IDADE DO DICIONARIO
#
# filme = {
#     'titulo':'Star Wars',
#     'ano':1977,
#     'diretor':'George Lucas'
# }
#
# print(filme.values())       # IMPRIME OS VALORES DO DICIONÁRIOS
# print(filme.keys())         # IMPRIME AS CHAVES (KEYS)
# print(filme.items())        # IMPRIME OS VALORES E AS CHAVES (KEYS)
#

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 41}
# print(pessoas['nome'])           # IMPRIME O ELEMENTO DA CHAVE NOME
# print(pessoas['sexo'])           # IMPRIME O ELEMENTO DA CHAVE SEXO
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())            # IMPRIME AS CHAVES(KEYS) DO DICIONÁRIO
# print(pessoas.values())          # IMPRIME OS VALORES DE UM DICIONÁRIO
# print(pessoas.items())           # IMPRIME TANTO OS VALORES COMO AS CHAVES DE UM DICIONÁRIO
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 30
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {
#     'uf': 'Rio de Janeiro',
#     'sigla': 'RJ'
# }
# estado2 = {
#     'uf': 'São Paulo',
#     'sigla': 'SP'
# }
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()
