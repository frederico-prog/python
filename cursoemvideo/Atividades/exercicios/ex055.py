'''
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.
'''
print('-=-' * 12)
print('{:^35}'.format(' VERIFICAÇÃO DE PESO '))
print('-=-' * 12)

maior = menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
