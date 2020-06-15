'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COM PARÂMETRO E MOSTRE UMA
MENSAGEM COM TAMANHO ADAPTÁVEL.
EX.: ESCREVA('OLÁ, MUNDO!')
SAÍDA:
~~~~~~~~~~~~
OLÁ, MUNDO!
~~~~~~~~~~~~
'''


def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# PROGRAMA PRINCIPAL
escreva('Aproveitando o isolamento social para aprender PYTHON!')
escreva('Curso de Python')
escreva('#FicaEmCasa')
