import sys

argumentos = sys.argv   # arg1 método // arg2 - n1 // arg3 - n2


def soma(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


try:
    if argumentos[1] == "soma":
        resp = soma(float(argumentos[2]), float(argumentos[3]))
    elif argumentos[1] == "subtrair":
        resp = subtrair(float(argumentos[2]), float(argumentos[3]))
    print(resp)
except IndexError:
    print('Quantidade de argumentos inválido.')
finally:
    print('OBRIGADO!!!')

