'''
22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele
é divisível.
'''
import random
num = random.randint(1, 100)
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