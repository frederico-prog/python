import time


def abre_arquivo():
    try:
        open('arquivotxt.txt')
        return True
    except Exception as erro:
        print('Ocorreu um erro:', erro)
        return False


while not abre_arquivo():
    print('Tentando abrir o arquivo.')
    time.sleep(5)

print('Arquivo aberto')