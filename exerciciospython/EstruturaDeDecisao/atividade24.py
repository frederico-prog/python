'''
24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado
da operação deve ser acompanhado de uma frase que diga se o número é:
    a- par ou ímpar;
    b- positivo ou negativo;
    c- inteiro ou decimal.
'''
n1 = str(input('Informe o primeiro número: ')).replace(',', '.')
n2 = str(input('Informe o segundo número: ')).replace(',', '.')

num1 = float(n1)
num2 = float(n2)

print(type(num1))

opc = int(input('Informe uma das opções:\n1- Par ou Ímpar\n2- Positivo ou Negativo\n3- Inteiro ou Decimal\n'))

# Opção 1: Verifica se o número é par ou ímpar
if opc == 1:
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(f'Os números {num1:.2f} e {num2:.2f} são pares.')
    elif num1 % 2 > 0 and num2 % 2 > 0:
        print(f'Os números {num1:.2f} e {num2:.2f} são ímpares.')
    elif num1 % 2 == 0 and num2 % 2 > 0:
        print(f'O número {num1:.2f} é par e o {num2:.2f} é ímpar.')
    elif num1 % 2 > 0 and num2 % 2 == 0:
        print(f'O número {num1:.2f} é ímpar e o {num2:.2f} é par.')
# Opção 2: Verifica se o número é positivo ou negativo
elif opc == 2:
    if num1 > 0 and num2 > 0:
        print(f'Os números {num1:.2f} e {num2:.2f} são positivos.')
    elif num1 < 0 and num2 < 0:
        print(f'Os números {num1:.2f} e {num2:.2f} são negativos.')
    elif num1 > 0 and num2 < 0:
        print(f'O número {num1:.2f} é positivo e o {num2:.2f} é negativo.')
    elif num1 < 0 and num2 > 0:
        print(f'O número {num1:.2f} é negativo e o {num2:.2f} é positivo.')
# Opção 3: Verifica se o número é inteiro ou decimal
elif opc == 3:
    pass
else:
    print('Opção inválida.')
