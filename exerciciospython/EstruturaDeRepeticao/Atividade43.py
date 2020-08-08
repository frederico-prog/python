'''
43 - O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser
encerrado.
'''
import random

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'cinza': '\033[37m',
         'verde': '\033[32m',
         'azul': '\033[34m'
         }


# Menu incial
print(' ')
print(f'{cores["azul"]} -{cores["limpa"]}' * 17, end='')
print(f'{cores["azul"]} LANCHONETE PYTHON {cores["limpa"]}'.center(20), end='')
print(f'{cores["azul"]} -{cores["limpa"]}' * 17)
print(' ')

lista_menu = [
    [100, 'Cachorro Quente', 1.20],
    [101, 'Bauru Simples', 1.30],
    [102, 'Bauru com ovo', 1.50],
    [103, 'Hamburger    ', 1.20],
    [104, 'Cheeseburguer', 1.30],
    [105, 'Refrigerante   ', 1.00]
]

lista_item = {}
lista_pedido = lista_fechamento_pedido = []
qtde = custo_item = custo = 0

# Imprime o cardápio
print('-' * 40)
print(f'CARDÁPIO'.center(35))
print('-' * 40)

print('Código\t Especificação\t\t\t Valor')
for codigo in lista_menu:
    print(codigo[0], ' \t', end=' ')
    print(codigo[1], ' \t\tR$', end=' ')
    print(f'{codigo[2]:.2f}', end=' ''\n')
print('-' * 40)

while True:
    # Inclusão do pedido
    pedido = random.randint(1000, 9999)

    # Inclusão do item de cada pedido
    while True:
        lista_item.clear()
        codigo = int(input('Informe o código do produto: '))

        for cod in lista_menu:
            if codigo in cod:
                qtde = int(input('Informe a quantidade solicitada: '))
                custo = cod[2] * qtde
                lista_item['item'] = cod[1]
                lista_item['custo_item'] = cod[2]

        lista_item['pedido'] = pedido
        lista_item['codigo'] = codigo
        lista_item['qtde'] = qtde
        lista_item['custo'] = custo

        lista_pedido.append(lista_item.copy())

        opc = str(input(f'Deseja inserir um novo item ao pedido {pedido}? "C" para continuar ou "S" para sair. ')).upper()[0]
        while opc not in 'CS':
            opc = str(input(f'Deseja inserir um novo item ao pedido {pedido}? "C" para continuar ou "S" para sair. ')).upper()[
                0]

        if opc == 'S':
            print('Encerrando o cadastro dos itens...')
            break

    opc1 = str(input('Deseja cadastrar um novo pedido? "C" para continuar ou "S" para sair. ')).strip().upper()[0]
    while opc1 not in 'CS':
        opc1 = str(input('Deseja cadastrar um novo pedido? "C" para continuar ou "S" para sair. ')).strip().upper()[0]

    if opc1 == 'S':
        print('Encerrando os pedidos...')
        break

# Encerramento da conta
print(lista_pedido)
for valor in lista_pedido:
    print(valor)
