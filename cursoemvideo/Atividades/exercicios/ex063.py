'''
Escreva um programa que leia um nº qualquer inteiro e mostre na tela os n primeiros elementos de uma Sequência de
Fibinacci
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
print('-=-' * 20)
print('{:^60}'.format(' SÉRIE DE FIBONACCI '))
print('-=-' * 20)

n = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('\n***** FIM DA EXECUÇÃO *******')
'''
anterior = 0
proximo = 0

num = int(input('Insira o valor digitado: '))

while proximo < num:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior

    if proximo == 0:
        proximo = proximo + 1
'''

