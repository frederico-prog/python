'''
23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados
o funcionamento, o estilo e o número de testes (divisões) executados
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