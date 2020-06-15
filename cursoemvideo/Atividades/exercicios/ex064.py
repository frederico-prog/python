'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos nº foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''
print('-=-' * 20)
print('{:^60}'.format(' TRATANDO VÁRIOS VALORES 1 - v1.0 '))
print('-=-' * 20)

print('\033[32mDigite uma série de números ou 999 para sair.\033[m')

sair = False
count = soma = 0

while not sair:
    num = float(input('\033[32mInsira o número desejado ou digite 999 para sair: \033[m'))

    if num == 999:
        sair = True
    else:
        count += 1
        soma += num

print('A soma foi {:.2f}. E você digitou {:.0f} números.'.format(soma, count))
