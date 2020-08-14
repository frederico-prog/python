'''
16 - Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9% de suas vendas brutas
daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9% de $3000,
ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:
    a - $200 - $299
    b - $300 - $399
    c - $400 - $499
    d - $500 - $599
    e - $600 - $699
    f - $700 - $799
    g - $800 - $899
    h - $900 - $999
    i - $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''
from time import sleep

resposta = ''
lista_venda_custo = []
premiacao = 9

# PREENCHE AS LISTAS lista_venda E lista_venda_custo COM O VENDEDOR E O VALOR DAS VENDAS DIÁRIA
while resposta != 'S':
    lista_venda = []
    soma_venda = 0
    venda = 0

    vendedor = str(input('Informe o nome do vendedor: ')).upper()
    lista_venda.append(vendedor)

    print(f'Informe as vendas do vendedor {vendedor} desta semana:')
    while venda != -1:
        venda_str = str(input('Informe os valores das compras: $ ')).replace(',', '.')
        venda = float(venda_str)

        soma_venda += venda

        lista_venda.append(venda)

        if venda == -1:
            break

    lista_venda.append(soma_venda)
    lista_venda_custo.append(lista_venda)

    resposta = str(input('Digite "S" para visualizar o valor dos pagamentos ou QUALQUER LETRA PARA CONTINUAR: ')).upper()

    if resposta == 'S':
        break

# DECLARAÇÃO DAS VARIÁVEIS PARA CONTAGEM DE CADA MÉDIA
count_int_200_299 = 0
count_int_300_399 = 0
count_int_400_499 = 0
count_int_500_599 = 0
count_int_600_699 = 0
count_int_700_799 = 0
count_int_800_899 = 0
count_int_900_999 = 0
count_acima_1000 = 0

# DECLARAÇÃO DAS LISTAS QUE ARMAZENA OS NOMES DOS VENDEDORES CONFORME SEUS PAGAMENTOS
lista_resultado1 = []
lista_resultado2 = []
lista_resultado3 = []
lista_resultado4 = []
lista_resultado5 = []
lista_resultado6 = []
lista_resultado7 = []
lista_resultado8 = []
lista_resultado9 = []

print('CALCULANDO OS PAGAMENTOS...')
sleep(1)
# CALCULA AS MÉDIAS DE PAGAMENTO
for vendedor in lista_venda_custo:
    total_venda = vendedor[-1]
    pagamento = 200 + (total_venda * (premiacao / 100))

    if pagamento <= 200 or pagamento <= 299:
        count_int_200_299 += 1
        lista_resultado1.append(vendedor[0])
    elif 300 <= pagamento <= 399:
        count_int_300_399 += 1
        lista_resultado2.append(vendedor[0])
    elif 400 <= pagamento <= 499:
        count_int_400_499 += 1
        lista_resultado3.append(vendedor[0])
    elif 500 <= pagamento <= 599:
        count_int_500_599 += 1
        lista_resultado4.append(vendedor[0])
    elif 600 <= pagamento <= 699:
        count_int_600_699 += 1
        lista_resultado5.append(vendedor[0])
    elif 700 <= pagamento <= 799:
        count_int_700_799 += 1
        lista_resultado6.append(vendedor[0])
    elif 800 <= pagamento <= 899:
        count_int_800_899 += 1
        lista_resultado7.append(vendedor[0])
    elif 900 <= pagamento <= 999:
        count_int_900_999 += 1
        lista_resultado8.append(vendedor[0])
    else:
        count_acima_1000 += 1
        lista_resultado9.append(vendedor[0])

# IMPRIME OS VENDEDORES E O TOTAL DE CADA MÉDIA DE PAGAMENTO
if count_int_200_299 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado1:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS ENTRE $200 E $ 299. TOTAL DE: {count_int_200_299}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $200 E $ 299.')

if count_int_300_399 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado2:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $300 E $ 399. TOTAL DE: {count_int_300_399}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $300 E $ 399.')

if count_int_400_499 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado3:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $400 E $ 499. TOTAL DE: {count_int_400_499}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $400 E $ 499.')

if count_int_500_599 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado4:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $500 E $ 599. TOTAL DE: {count_int_500_599}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $500 E $ 599.')

if count_int_600_699 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado5:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $600 E $ 699. TOTAL DE: {count_int_600_699}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $600 E $ 699.')

if count_int_700_799 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado6:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $700 E $ 799. TOTAL DE: {count_int_700_799}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $700 E $ 799.')

if count_int_700_799 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado7:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $800 E $ 899. TOTAL DE: {count_int_800_899}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $800 E $ 899.')

if count_int_700_799 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado8:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ENTRE $900 E $ 999. TOTAL DE: {count_int_900_999}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ENTRE $900 E $ 999.')

if count_acima_1000 > 0:
    print('VENDEDORES', end=' ')
    for v in lista_resultado9:
        print(f'{v}', end=',')
    print(f'TIVERAM SALÁRIOS SALÁRIOS ACIMA DE $ 1000. TOTAL DE: {count_acima_1000}')
else:
    print(f'NÃO HOUVERAM PAGAMENTOS ACIMA DE $ 1000.')
