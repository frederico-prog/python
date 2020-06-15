'''
CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR
SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL, MOSTRE:
A- QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
B- QUANTOS HOMENS FORAM CADASTRADOS.
C- QUANTAS MULHEREES TEM MENOS DE 20 ANOS.
'''
import emoji
print('-=-' * 12)
print('{:^35}'.format(' ANALISE DE DADOS DE GRUPO '))
print('-=-' * 12)

countmaior18 = counthomem = countmulher = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
    tipo = ' '
    while tipo not in 'CS':
        tipo = str(input('Deseja continuar? Digite "C" para continuar ou "S" para sair [C/S]')).strip().upper()[0]
    if tipo == 'S':
        break
    if idade >= 18:
        countmaior18 += 1
    if sexo == 'M':
        counthomem += 1
    if idade < 20 and sexo == 'F':
        countmulher += 1
print(f'Total de pessoas acima de 18 anos: {countmaior18}'
      f'\nTotal de homens cadastrados: {counthomem}'
      f'\nTotal de mulheres com idade abaixo de 20 anos: {countmulher} ')
print('FIM DA EXECUÇÃO!!!!')
