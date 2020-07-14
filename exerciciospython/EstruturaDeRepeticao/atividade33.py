'''
33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
'''
resp = 'S'
maior = menor = media = soma = count = 0

while resp in 'Ss':
    estado = str(input('Informe o Estado: ')).upper()
    temp = str(input(f'Informe a temperatura do Estado {estado}: ')).replace(',', '.')
    temperatura = float(temp)

    soma += temperatura
    count += 1

    estadomenor = ''
    estadomaior = ''

    if count == 1:
        maior = menor = temperatura
        estadomaior = estado
        estadomenor = estado
    else:
        if temperatura > maior:
            maior = temperatura
            estadomaior = estado
        if temperatura < menor:
            menor = temperatura
            estadomenor = estado

    resp = str(input('Deseja cadastrar uma nova temperatura? "S" para continuar "N" para sair. ')).upper().strip()[0]

media = soma / count
print(f'A soma das temperatura foi: {soma:.2f}ºC.')
print(f'A média das temperatura foi: {media:.2f}ºC.')
print(f'A maior temperatura registrada foi do Estado de {estadomaior} com a temperatura de {maior:.2f}ºC.')
print(f'A menor temperatura registrada foi do Estado de {estadomenor} com a temperatura de {menor:.2f}ºC.')
