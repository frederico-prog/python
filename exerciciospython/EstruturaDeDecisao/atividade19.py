'''
19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
import math

while True:
    num = int(input('Digite um valor qualquer com até 3 digitos: '))
    valor = num
    digitos = int(math.log10(valor)) + 1

    if digitos > 3:
        print(f'O número digitado {valor} está fora do limite.')
    else:
        # Unidade
        unidade = valor % 10
        # Dezena
        valor = (valor - unidade) / 10
        dezena = valor % 10
        # Centena
        valor = (valor - dezena) / 10
        centena = valor % 100

        # Converte os resultados para inteiro
        dezena = int(dezena)
        centena = int(centena)

    # Verifica se a Centena e a Dezena são iguais a Zero ou a Um
    if unidade == 0 or unidade == 1:
        flexaoUnidade = 'unidade'
    else:
        flexaoUnidade = 'unidades'

    if dezena == 0 or dezena == 1:
        flexaoDezena = 'dezena'
    else:
        flexaoDezena = 'dezenas'

    if centena == 0 or centena == 1:
        flexaoCentena = 'centena'
    else:
        flexaoCentena = 'centenas'

    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
        print(resp)
        if resp == 'N':
            break

    # Imprime os resultados
    if digitos == 3:
        print(f'{num}: {centena} {flexaoCentena}, {dezena} {flexaoDezena} e {unidade} {flexaoUnidade}.')
    elif digitos == 2:
        print(f'{num}: {dezena} {flexaoDezena} e {unidade} {flexaoUnidade}.')
    else:
        print(f'{num}: {unidade} {flexaoUnidade}.')
