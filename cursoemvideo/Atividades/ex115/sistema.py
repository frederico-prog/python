'''
from PythonExercicios.ex115.lib.interface import *
from PythonExercicios.ex115.lib.arquivo import *
'''
from time import sleep
from ex115.lib.arquivo import *
from ex115.lib.interface import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de lsitar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção para sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        #Indica que a opção digita é inexistente
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
