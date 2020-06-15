'''
APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
A- A SOMA DE TODOS OS VALORES DIGITADOS
B- A SOMA DOS VALORES DA TERCEIRA COLUNA
C- O MAIOR VALOR DA SEGUNDA LINHA
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for l in range(0, 3):                  # FOR para a linha
    for c in range(0, 3):              # FOR para a coluna
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-*-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-*-' * 30)
print(f'A soma dos números pares foram: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos números da coluna 3 é de {scol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é o {maior}')
