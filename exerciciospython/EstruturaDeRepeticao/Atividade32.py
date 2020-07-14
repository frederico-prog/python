'''
32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída
deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! = 5 . 4 . 3 . 2 . 1 = 120
'''

num = int(input('Digite um número: '))
numCalc = num
fatorial = 1

print(f'Fatorial de: {num}')

while numCalc > 0:
    fatorial *= numCalc
    if numCalc > 1:
        print(f'{num} . {numCalc}')
    else:
        print(numCalc)
    numCalc -= 1

print(f'Resultado Fatorial de {num}! = {fatorial}')
