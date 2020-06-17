'''
18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
import time

data = str(input('Digite a data desejada no formato dd/mm/aaaa: ')).strip()
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

validade = True
i = 0

print('Analisando....')
time.sleep(1)

while validade == True and i == 0:
    # Valida o ano
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        bissexto = 'Sim'
    else:
        bissexto = 'Não'

    if ano < 1900:
        validade = False

    # Valida o mês
    if mes < 1 or mes > 12:
        validade = False

    if (mes == 2 and bissexto == 'Não' and dia > 28) or (mes == 2 and bissexto == "sim" and dia > 29):
        validade = False

    # Valida o dia
    if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
        validade = False

    i += 1

if validade:
    print(f'A data {data} é válida!')
else:
    print(f'A data {data} não é válida!')
