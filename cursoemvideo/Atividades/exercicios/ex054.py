'''
Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maior
idade e quantos já são maiores.
'''
from datetime import date
print('-=-' * 12)
print('{:^35}'.format(' VERIFICAÇÃO DA MAIOR E MENOR IDADE '))
print('-=-' * 12)

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade.'.format(totmenor))



