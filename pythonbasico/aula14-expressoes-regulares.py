'''
r - RAW String
. - pesquisa qualquer tipo de palavra e espaços
\w - palavras de A a Z maiuscula e de a a z minusculas
+ - excuta mais de uma vez a operação
'''
import re
import requests

#string_teste = 'O gato é bonito'
#padrao = re.search(r'gat.', string_teste)
# string_teste = 'O gato, a gata, os gatinhoes e os gatões são bonitos.'
# padrao = re.findall(r'gat\w', string_teste)
# if padrao:
#     print(padrao)
# else:
#     print('Padrão não encontrado!')
# print(r'Oi pessoal!\nSegunda linha.')

string = 'https://www.meiaoito.com.br'
requisicao = requests.get(string)
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')

