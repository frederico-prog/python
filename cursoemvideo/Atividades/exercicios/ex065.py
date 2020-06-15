'''
Crie um programa que leia vários nº inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valor lido. O programa deve perguntar para o usuário se ele quer ou não continuar a digitar
valores.
'''
print('-=-' * 20)
print('{:^60}'.format(' TRATANDO VÁRIOS VALORES 2 - v1.0 '))
print('-=-' * 20)

resp = 'S'
count = media = maior = soma = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / count
print('Foram digitados {} números'.format(count))
print('A média dos nº digitado foi {} e a soma deles é de {}.'.format(media, soma))
print('O maior nº digitado foi {} e o menor digitado foi o {}.'.format(maior, menor))

