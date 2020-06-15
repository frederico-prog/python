'''
FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR
DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
'''
print('INSIRA 5 VALORES NUMÉRICOS')
num = []
pos_maior = []
pos_menor = []
for c in range(0, 5):
    num.append(int(input(f'{c + 1}º número: ')))
for pos, valor in enumerate(num):
    if valor == max(num):
        pos_maior.append(pos)
    if valor == min(num):
        pos_menor.append(pos)
print('*' * 35)
print(f'Você digitou os seguintes números: {num}.')
print(f'O maior número foi o {max(num)} e ele está na posição {pos_maior}.')
print(f'O menor número foi o {min(num)} e ele está na posição {pos_menor}.')
