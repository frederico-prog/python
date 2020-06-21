'''
13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem.
'''
base = int(input('Informe o número que será a base para o cálculo: '))
expoente = int(input('Inforome o número que será o exponte para o cálculo: '))

count = 0
resp = 1

if base == 0:
    print('Zero elevado a qualquer número sempre é zero.')
    print(f'{base} elevado à {expoente} = 0')
elif expoente == 1:
    print(f'Todo número elevado a {expoente} é ele mesmo.')
    print(f'{base} elevado à {expoente} = {base}')
elif expoente == 0:
    print(f'Todo número elevado a {expoente} sempre é um.')
    print(f'{base} elevado à {expoente} = 1')
else:
    while count < expoente:
        resp = base * resp
        count += 1

print(f'{base} elevado à {expoente} = {resp}')
