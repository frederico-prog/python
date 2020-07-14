'''
28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
quantCD = int(input('Digite a quantidade de CDs: '))
print('')

a = 0
valorTotal = 0

for x in range(quantCD):
    valorCD = eval(input('Digite o valor do CD: '))
    valorTotal = valorTotal + valorCD
    valorMedio = valorTotal / quantCD
    a += 1

print('')
print(f'O valor total gasto: R$ {valorTotal}')
print(f'O valor médio gasto por cada CD foi de: R$ {valorMedio}')

# colecao_cd = dict()
# lista_cd = list()
# custo_cd = list()
#
#
# print('Informe a quantidade de Cds e o valor gasto para cada um deles')
#
# while True:
#     count = 0
#     colecao_cd['nome'] = str(input('Informe o nome da sua coleção de CDs: ')).upper()
#     colecao_cd['quantidade'] = int(input('Informe a quantidade de CDs a sua coleção possui: '))
#
#     while count < colecao_cd['quantidade']:
#         valor_str = str(input(f'Informe o valor de cada CD: {count + 1} ')).replace(',', '.').strip()
#         valor = float(valor_str)
#         custo_cd.append(valor)
#         colecao_cd['valor'] = custo_cd
#         count += 1
#
#     lista_cd.append(colecao_cd.copy())
#     colecao_cd.clear()
#
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja cadastrar uma nova coleção? 'S' para continuar e 'N' para sair. ')).upper().strip()[0]
#
#     if resp == 'N':
#         break
#
# print(lista_cd)
