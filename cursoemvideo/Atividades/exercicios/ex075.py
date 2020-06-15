'''
DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
A- QUANTAS VEZES APARECEU O VALOR 9.
B- EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
C- QUAIS FORAM OS NÚMEROS PARES.
'''
num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
