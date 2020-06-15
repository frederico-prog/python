'''
CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO.
NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):                  # FOR para a linha
    for c in range(0, 3):              # FOR para a coluna
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-*-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

