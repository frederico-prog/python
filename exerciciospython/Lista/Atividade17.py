'''
17 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser
encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''
lista_atletas = []
soma_salto = media_salto = 0
resposta = ''

while resposta != 'S':
    lista_saltos = []

    atleta = str(input('Informe o nome do atleta: ')).capitalize()
    lista_saltos.append(atleta)

    for tentativa in range(0, 5):
        salto_str = str(input(f'Informe a distânica da {tentativa + 1}ª tentativa: ')).replace(',', '.')
        salto = float(salto_str)
        lista_saltos.append(salto)

    lista_atletas.append(lista_saltos)

    resposta = str(input('Para cadastrar um novo atleta digite "C" ou para sair "S": ')).upper()

    if resposta == 'S':
        break

print(lista_atletas)

for parcial in lista_atletas:
    print('')
    print(f'Atleta: {parcial[0]}')
    print('')
    print(f'Primeiro salto: {parcial[1]}')
    print(f'Segundo salto: {parcial[2]}')
    print(f'Terceiro salto: {parcial[3]}')
    print(f'Qarto salto: {parcial[4]}')
    print(f'Quinto salto: {parcial[5]}')
print('')
print('Resultado final:')
for key, value in enumerate(lista_atletas):
    if key == 0:
        soma_salto = value[1] + value[2] + value[3] + value[4] + value[5]
        media_salto = soma_salto / 5
        print(f'Atleta: {value[0]}')
        print(f'Saltos: {value[1]} - {value[2]} - {value[3]} - {value[4]} - {value[5]}')
        print(f'Média dos saltos: {media_salto}')
    else:
        print('')
        soma_salto = value[1] + value[2] + value[3] + value[4] + value[5]
        media_salto = soma_salto / 5
        print(f'Atleta: {value[0]}')
        print(f'Saltos: {value[1]} - {value[2]} - {value[3]} - {value[4]} - {value[5]}')
        print(f'Média dos saltos: {media_salto}')


