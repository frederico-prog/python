'''
CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA
SEPARADOS OS VALORES PARES E ÍMPARES. NO FINAL, MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE.
'''
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-*-' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
