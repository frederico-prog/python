'''
CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE À FUNÇÃO INPUT() DO PYTHON, SÓ QUE
FAZENDO A A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO.
EX.: N = LEIAINT('DIGITE UM NÚMERO')
'''


def leiaInt(msg):
    validador = False
    numero = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            numero = int(n)
            validador = True
        else:
            print('\033[0:31mERRO! Digite um número válido.\033[m')
        if validador:
            break
    return numero


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Vocâ acabou de digitar o valor {n}')
