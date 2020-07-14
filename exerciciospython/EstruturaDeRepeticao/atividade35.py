'''
35 - Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
'''
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print(f'O número {num} é PRIMO!')
else:
    print(f'O número {num} não é PRIMO!')

print('***** FIM DA EXECUÇÃO *****')
