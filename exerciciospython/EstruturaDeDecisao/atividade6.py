'''
6 - Faça um Programa que leia três números e mostre o maior deles.
'''
num1 = str(input('Insira o primeiro número: ')).replace(',', '.')
num2 = str(input('Insira o segundo número: ')).replace(',', '.')
num3 = str(input('Insira o terceiro número: ')).replace(',', '.')

parsernum1 = float(num1)
parsernum2 = float(num2)
parsernum3 = float(num3)

if parsernum1 > parsernum2 and parsernum1 > parsernum3:
    print(f'O número {parsernum1:.2f} é o maior deles.')
elif parsernum1 < parsernum2 and parsernum2 > parsernum3:
    print(f'O número {parsernum2:.2f} é o maior deles.')
else:
    print(f'O número {parsernum3:.2f} é o maior deles.')
