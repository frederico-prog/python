'''
10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
por eles.
'''
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 < num2:
    for num in range(num1 + 1, num2):
        print(num, end=', ')
elif num2 > num1:
    for num in range(num2, num1 + 1, -1):
        print(num, end=', ')
elif num1 == num2:
    print('Os números são iguais!')
else:
    print('Sequência digita inválida!')
