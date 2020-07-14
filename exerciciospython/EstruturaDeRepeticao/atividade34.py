'''
34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
ou não um número primo.
'''
num = int(input('Digite um número inteiro: '))

x = 2
a = 0

while x < num:
    if num % x == 0:
        a = 0
        x = num
    else:
        x += 1
        a = 1

if a == 1 or num == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')
