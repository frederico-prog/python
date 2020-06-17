'''
26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    1- Álcool:
        a- até 20 litros, desconto de 3% por litro
        b- acima de 20 litros, desconto de 5% por litro
    2- Gasolina:
        a- até 20 litros, desconto de 4% por litro
        b- acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool,
G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.
'''
# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'cinza': '\033[37m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'azul': '\033[34m'
         }

# Declaração das variáveis
descontoalcool3 = 0.03
descontoalcool20 = 0.05
precoalcool = 1.90

descontogas3 = 0.04
descontogas20 = 0.06
precogas = 2.50

combustivel = ''

print(f'{cores["verde"]} POSTO DE GASOLINA PYTHON {cores["limpa"]}'.center(40))

print('Selecione uma das opções abaixo:')
menu = str(input(f'{cores["cinza"]}A - Álccol\nG - Gasolina{cores["limpa"]}\n')).upper().strip()

# Verifica o tipo do combustível e calcula o custo para pagamento
# A - Álcool
if menu == 'A':
    qtde = str(input('Informe o total de litros abastecidos: ')).replace(',', '.').strip()
    litro = float(qtde)
    if litro <= 20:
        custo = precoalcool * litro
        desconto = custo * descontoalcool3
        pagamento = custo - desconto
    elif litro > 20:
        custo = precoalcool * litro
        desconto = custo * descontoalcool20
        pagamento = custo - desconto
# G - Gasolina
elif menu == 'G':
    qtde = str(input('Informe o total de litros abastecidos: ')).replace(',', '.').strip()
    litro = float(qtde)
    if litro <= 20:
        custo = precogas * litro
        desconto = custo * descontogas3
        pagamento = custo - desconto
    elif litro > 20:
        custo = precogas * litro
        desconto = custo * descontogas20
        pagamento = custo - desconto
else:
    print(f'{cores["vermelho"]}Opção inválida!{cores["limpa"]}')

# Imprime o resultado para o cliente
print(' ')
print('POSTO DE GASOLINA PYTHON'.center(32))
print('NOTA FISCAL'.center(35))

# Verifca o tipo de combustível para mostrar o cliente
if menu == 'A':
    combustivel = 'Álcool'
else:
    combustivel = 'Gasolina'

print(f'Combustível...............\t{combustivel}')
print(f'Litros....................\t{litro:.2f}l')

# Verifca o tipo de combustível para mostrar ao cliente o custo sem desconto para o cliente
if menu == 'A':
    print(f'Preço.....................\tR$ {precoalcool:.2f}')
else:
    print(f'Preço.....................\tR$ {precogas:.2f}')

print(f'Custo.....................\tR$ {custo:.2f}')
print(f'Desconto..................\tR$ {desconto:.2f}')
print(f'Pagamento.................\tR$ {pagamento:.2f}')
print(' ')
print(f'{cores["vermelho"]}OBRIGADO PELA PREFERÊNCIA. VOLTE SEMPRE!!!{cores["limpa"]}')
