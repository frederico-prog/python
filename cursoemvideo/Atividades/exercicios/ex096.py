'''
FAÇA UM PROGAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR(LARGURA E
COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.
'''


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno com {largura}m² x {comprimento}m² é de {area:.2f}m².')


# PROGRAMA PRINCIPAL
titulo('   CONTROLE DE COMPRIMENTO   ')
largura = float(input('Informe a largura do terreno em m²: '))
comprimento = float(input('Informe o comprimento do terreno em m²: '))
area(largura, comprimento)
