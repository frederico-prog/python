'''
27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
'''
import time

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'azul': '\033[34m'
         }

# Declaração das variáveis
precomaca5 = 1.80
precomacamais5 = 1.50

precomorango5 = 2.50
precomorangomais5 = 2.20

descontopromofruta = 0.10

kilopromocao = 8
precopromocao = 25

pagosemdesconto = desconto = peso = pago = 0

# Menu
print(' ')
print(f'{cores["azul"]} -{cores["limpa"]}' * 20, end='')
print(f'{cores["azul"]}FRUTEIRA PYTHON{cores["limpa"]}'.center(25), end='')
print(f'{cores["azul"]} -{cores["limpa"]}' * 20)
print(' ')


fruta = str(input('Informe a fruta comprada: "MAÇÂ" e/ou "MORANGO": ')).upper()

# Verifica o tipo de fruta comprada pelo cliente MAÇÂ ou MORANGO
if fruta in 'MACAMAÇÃMAÇAMACÃ':
    p = str(input('Informe o peso: ')).replace(',', '.')
    peso = float(p)
    time.sleep(1)

# Verifica o peso comprado pelo cliente
    if peso <= 5:
        pagosemdesconto = peso * precomaca5
    elif peso > 5 or peso <= 7:
        pagosemdesconto = peso * precomacamais5

    if peso >= 8 or pagosemdesconto >= 25:
        pagosemdesconto = peso * precomacamais5
        desconto = pagosemdesconto * descontopromofruta
        pago = pagosemdesconto - desconto
elif fruta == 'MORANGO':
    p = str(input('Informe o peso: ')).replace(',', '.')
    peso = float(p)
    time.sleep(1)

    # Verifica o peso comprado pelo cliente
    if peso <= 5:
        pagosemdesconto = peso * precomorango5
    elif peso > 5 or peso <= 7:
        pagosemdesconto = peso * precomorangomais5

    if peso >= kilopromocao or pagosemdesconto >= precopromocao:
        pagosemdesconto = peso * precomorangomais5
        desconto = pagosemdesconto * descontopromofruta
        pago = pagosemdesconto - desconto
else:
    print(f'A fruta {fruta} não está disponível no sistema.')

# Impressão da nota fiscal para o cliente
print(' ')
print('-' * 43)
print('FRUTEIRA PYTHON'.center(37))
print('NOTA FISCAL'.center(35))
print('-' * 43)
print(' ')

# Imprime o nome da fruta MAÇÂ de forma correta, desconsiderando com o operador o digitou.
if fruta in 'MACAMAÇÃMAÇAMACÃ':
    frutacorreta = 'MAÇÃ'
    print(f'Fruta\t...................\t{frutacorreta}')
else:
    print(f'Fruta\t...................\t{fruta}')

print(f'Peso\t...................\t{peso:.2f}kg')
print(f'Preço\t...................\tR$ {pagosemdesconto:.2f}')

# Somente será impresso o DESCONTO e o PAGAMENTO caso o cliente tenha comprado acima de 8 kilos ou acima de R$ 25.00
if desconto == 0 and pago == 0:
    pass
else:
    print(f'Desconto\t...............\tR$ {desconto:.2f}')
    print(f'Pagamento\t...............\tR$ {pago:.2f}')

print(' ')
print('OBRIGADO PELA PREFERÊNCIA. VOLTE SEMPRE!!!')
