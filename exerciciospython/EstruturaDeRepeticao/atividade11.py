'''
11 - Altere o programa anterior para mostrar no final a soma dos números.
'''
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

lista = []
count = 0

if num1 < num2:
    for num in range(num1 + 1, num2):
        lista.append(num)
        count += 1
elif num2 > num1:
    for num in range(num2, num1 + 1, -1):
        lista.append(num)
        count += 1
elif num1 == num2:
    print('Os números são iguais!')
else:
    print('Sequência digita inválida!')

soma = sum(lista)
print(f'Números listados entre {num1} e {num2}: {lista}')
print(f'A soma entre os números {num1} e {num2} é: {soma}')
print(f'Entre os {num1} e {num2} foram encontrados: {count}')
