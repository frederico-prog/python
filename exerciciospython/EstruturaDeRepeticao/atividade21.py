'''
21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1.
'''
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} foi divisível por {total} vezes.')
if total == 2:
    print(f'{num} é PRIMO!')
else:
    print(f'{num} não é PRIMO!')

print('***** FIM DA EXECUÇÃO DO PROGRAMA *****')