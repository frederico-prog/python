'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''
print('-=-' * 12)
print('{:^35}'.format(' SISTEMA DE VERIFCAÇÃO '))
print('-=-' * 12)

somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('------------ {}ª PESSOA -------------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mas velho tem {} anos e se chama {}'.format(maioridadehome, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
