'''
CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO.
DEPOIS MOSTRE:
A- APENAS OS 5 PRIMEIROS COLOCADOS. (FATEAMENTO DAS TUPLAS)
B- OS ÚLTIMOS 4 COLOCADOS DA TABELA. (FATEAMENTO DAS TUPLAS)
C- UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
D- EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE.
'''
print('-=-' * 20)
print('{:^60}'.format(' TABELA BRASILEIRÃO 2019 '))
print('-=-' * 20)
classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athetico-PR', 'São Paulo', 'Internacional', 'Corinthinas'
                 , 'Fortaleza', 'Goias', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
                 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('-*-' * 30)
print(f'Tabela do Brasileirão 2019: {classificacao}')
print('-*-' * 30)
print(f'Os 5 primeiros colocaddos do Brasileirão 2019 foram: {classificacao[:5]}')
print('-*-' * 30)
print(f'Os últimos 4 colocados do Brasileirão 2019 foram: {classificacao[16:]}')
print('-*-' * 30)
print(f'Ordem alfabética dos times: {sorted(classificacao)}')
print('-*-' * 30)
print('A Chpecoense ficou na {}ª posição do Brasileiro de 2019.'.format(classificacao.index('Chapecoense') + 1))
print('-*-' * 30)
print('\o/' * 5)

