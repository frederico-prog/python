'''
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado
for ímpar, desconsidere-o
'''
print('-=-' * 12)
print('{:^35}'.format(' SOMA DE NÚMEROS PARES '))
print('-=-' * 12)

soma = 0
c = 0
for count in range(1, 7):
    num = int(input('Digite o {}º número: '.format(count)))
    if num % 2 == 0:
        soma += num
        c += 1
print('Você informou {} números PARES e a soma foi: {}'.format(c, soma))

print('***** FIM DA EXECUÇÃO *******')
