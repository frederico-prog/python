'''
1 - Faça um Programa que peça dois números e imprima o maior deles.
'''
valor1 = str(input('Insira o primeiro valor: ')).replace(',', '.')
valor2 = str(input('Insira o segundo valor: ')).replace(',', '.')

num1 = float(valor1)
num2 = float(valor2)

if num1 > num2:
    print(f'O número {num1:.2f} é maior que o número {num2:.2f}.')
else:
    print(f'O número {num2:.2f} é maior que o número {num1:.2f}.')
