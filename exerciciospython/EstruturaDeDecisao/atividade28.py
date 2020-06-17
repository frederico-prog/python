'''
28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''
# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'cinza': '\033[37m',
         'verde': '\033[32m',
         'azul': '\033[34m'
         }

# Lista de carnes na promoção
lista_carnes = [
    [123, 'Filé Duplo', 4.9, 5.8],
    [789, 'Picanha', 6.9, 7.8],
    [456, 'Alcatra', 5.9, 6.8]
]

# Declaração das variáveis
descontocartao = 0.05
desconto = 0
valorkg = 0
custo = 0
peso = 0
run = True
compras = []
lista_compra = []

# Menu incial
print(' ')
print(f'{cores["azul"]} -{cores["limpa"]}' * 17, end='')
print(f'{cores["azul"]}HIPERMERCADO TABAJARA{cores["limpa"]}'.center(20), end='')
print(f'{cores["azul"]} -{cores["limpa"]}' * 17)
print(' ')

while run:
    compras.clear()

    codigo = int(input('Digite o código da carne: '))

    # Acessa a lista de carnes
    for carne in lista_carnes:

        if codigo in carne:
            qtdecarne = int(input(f'Informe a quantidade comprada para a carne {carne[1]}: '))

            # Verifica a quantidade de carne compra conforme o tipo
            if qtdecarne == 1:
                peso = float(input('Informe a quantidade comprada em KG: '))
                if peso <= 5:
                    valorkg = carne[2]
                    custo = valorkg * peso
                else:
                    valorkg = carne[3]
                    custo = valorkg * peso
            else:
                print(f'O cliente somente poderá levar uma única quantidade da carne {carne[1]}')

            # Usuário seleciona a forma de pagamento
            opc = str(input('Digite "C" para compras no cartão ou "D" para compras no dinheiro: ')).upper()

            if opc == 'C':
                desconto = custo * descontocartao
                pagamento = custo - desconto
            else:
                pagamento = custo

            compras.append(carne[1])
            compras.append(qtdecarne)
            compras.append(peso)
            compras.append(valorkg)

            if opc == 'C':
               compras.append(desconto)
            else:
                compras.append('NÃO HOUVE DESCONTO')

            compras.append(pagamento)

            if opc == 'C':
                compras.append('CARTÃO')
            else:
                compras.append('DINHEIRO')
#
            lista_compra.append(compras[:])

    nova_compra = input('Deseja cadastrar uma nova compra? (S = Sim, qualquer tecla = Não)').upper()
    run = True if nova_compra.upper() == 'S' else False

# # Impressão da nota fiscal para o cliente
print(' ')
print('-' * 43)
print('HIPERMERECADO TABAJARA'.center(37))
print('NOTA FISCAL'.center(35))
print('-' * 43)
print(' ')

for lista in lista_compra:
    print(f'Carne..................\t{lista[0]}')
    print(f'Quantidade.............\t{lista[1]}')
    print(f'Peso...................\t{lista[2]}KG')
    print(f'Preço..................\tR$ {lista[3]:.2f}')
    print(f'Desconto...............\tR$ {lista[4]:.2f}')
    print(f'Pagamento..............\tR$ {lista[5]:.2f}')
    print(f'Forma de pagamento.....\t{lista[6]}')

print(' ')
print('OBRIGADO PELA PREFERÊNCIA. VOLTE SEMPRE!!!')