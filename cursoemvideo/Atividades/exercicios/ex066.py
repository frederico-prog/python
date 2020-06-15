'''
CRIE UM PROGRAMA QUE LEIA VÁRIOS Nº INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR 999, QUE É A
CONDIÇÃO DE PARRADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERAR O FLAG)
'''
print('-=-' * 12)
print('{:^35}'.format(' TRATANDO VÁRIOS VALORES 1 - v2.0 '))
print('-=-' * 12)
count = s = media = 0
while True:
    n = int(input('Digite um nº (999 para parar): '))
    if n == 999:
        break
    s += n
    count += 1
    media = s / count
print(f'Soma {s} \nQtde: {count} \nMedia: {media}')
