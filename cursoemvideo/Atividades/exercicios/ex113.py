'''
REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104, INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE UM NÚMERO DE TIPO
INVÁLIDO. APROVEITE E CRIE TAMBÉM UMA FUNÇÃO LEIAFLOAT COM A MESMA FUNCIONALIDADE.
'''


def leiaInt(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            i = int(n)
        except (ValueError, TypeError):
            print('\033[0:31mERRO! Por favor, digite um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0:31mUsuário preferiu não digitar nenhum valor.\033[m')
            return 0
        else:
            return i


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg)).strip().replace(',', '.')
            f = float(n)
        except (ValueError, TypeError):
            print('\033[0:31mERRO! Por favor, digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0:31mUsuário preferiu não digitar nenhum valor. \033[m')
            return 0
        else:
            return f


# PROGRAMA PRINCIPAL
i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número decimal: ')
print(f'Vocâ digitou os valores {i} e {f}')
