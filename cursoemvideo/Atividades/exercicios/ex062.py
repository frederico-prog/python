'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar '0 termos'.
'''
from time import sleep
print('-=-' * 12)
print('{:^35}'.format(' PROGESSÃO ARITIMÉTICA(PA) - v3.0 '))
print('-=-' * 12)

primeiro = int(input('Informe o primeiro elemento: '))
razao = int(input('Razão da PA: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA...')
    sleep(0.5)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('\n***** FIM DA EXECUÇÃO *******')
