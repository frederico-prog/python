def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).upper().strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


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
