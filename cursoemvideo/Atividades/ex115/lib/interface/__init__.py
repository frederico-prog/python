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


def linha(tamanho=42):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
