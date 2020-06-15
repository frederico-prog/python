'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
utilizando a estrutura while.
'''
print('-=-' * 12)
print('{:^35}'.format(' PROGESSÃO ARITIMÉTICA(PA) - v2.0 '))
print('-=-' * 12)

primeiro = int(input('Informe o primeiro elemento: '))
razao = int(input('Razão da PA: '))
termo = primeiro
count = 1
while count <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    count += 1
print('\n***** FIM DA EXECUÇÃO *******')