# import requests
# import json
#
#
# def requisicao(titulo):
#     try:
#         req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=1d44ceaf&type=movie')
#         dicionario = json.loads(req.text)
#         return dicionario
#     except:
#         print('Erro na conexão')
#         return None
#
#
# def detalhes(filme):
#     print('Título:', filme['Title'])
#     print('Ano:', filme['Year'])
#     print('Diretor:', filme['Director'])
#     print('Atores:', filme['Actores'])
#     print('Nota:', filme['imdbRating'])
#     print('Prêmios:', filme['Awards'])
#     print('Poster:', filme['Poster'])
#     print('')
#
#
# sair = False
# while not sair:
#     op = str(input('Escreva o nome do filme ou SAIR para fechar: ')).upper().strip()
#
#     if op == 'SAIR':
#         sair = True
#         print('Saindo....')
#     else:
#         filme = requisicao(op)
#         if filme['Response'] == 'False':
#             print('Filme não encontrado')
#         else:
#             detalhes(filme)

'''
EXERCICIO
Fazer com que o programa realize a busca do filme digitado pelo cliente, e retorne todos os filmes encontrados.
'''
import requests
import json
import time


def lista_filmes(titulo):
    lista = []
    print('Pesquisando lista de filmes....')
    for i in range(1, 101):
        try:
            time.sleep(0.5)
            req = requests.get('http://www.omdbapi.com/?s=' + titulo + '&apikey=1d44ceaf&type=movie&page=' + str(i))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tituloFilme = filme['Title']
                    ano = filme['Year']
                    string = tituloFilme + '(' + ano + ')'
                    lista.append(string)
            else:
                break

        except:
            print('Conexão falhou!')
    return lista


sair = False
while not sair:
    op = str(input('Pesquise por um filme ou digite SAIR: ')).upper().strip()
    if op == 'SAIR':
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados:', len(lista_de_filmes))
        print('Listando os filmes encontrados.')
        for filme in lista_de_filmes:
            print(filme)
            time.sleep(0.5)
    print('FIM DA LISTA...')

