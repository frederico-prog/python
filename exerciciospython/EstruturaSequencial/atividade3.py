'''
3 - Faça um Programa que peça dois números e imprima a soma.
'''

num1 = str(input('Informe o primeiro número: '))
num2 = str(input('Informe o segundo número: '))

parsernum1 = float(str(num1).replace(',', '.'))
parsernum2 = float(str(num2).replace(',', '.'))

soma = parsernum1 + parsernum2

#print('A soma entre {} e {} é: {}'.format(parsernum1, parsernum2, soma))
print(f'A soma entre {parsernum1} e {parsernum2} é: {soma}')