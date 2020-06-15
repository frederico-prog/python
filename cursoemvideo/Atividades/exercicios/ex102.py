'''
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR
E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO(OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO
DO FATORIAL
'''


def fatorial(num, show=False):
    """
    -> Calcula o valor fatorial de um número n
    :param num: refere-se ao número que será calculado o fatorial
    :param show: define se o cálculo do fatorial será ou não mostrado
    return: retorna o resultado do cálculo do fatorial
    """
    f = 1
    if not show:
        for c in range(num, 0, -1):
            f *= c
    else:
        for c in range(num, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            f *= c
    return f


# PROGRAMA PRINCIPAL
num = int(input('Insira o número: '))
mostra = int(input('Informe 1(um) caso queira visualizar o cálculo ou 0(zero) para não visualizar o cálculo: '))
if mostra == 1:
    show = True
    print(fatorial(num, show))
else:
    print(print(fatorial(num)))

help(fatorial)
