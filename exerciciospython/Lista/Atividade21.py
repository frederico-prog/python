'''
21 - Faça um programa que carregue uma lista com os modelos de 5 carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro
de combustível. Calcule e mostre:
    a - O modelo do carro mais econômico;
    b - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000
    quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são
fictícios e podem mudar a cada execução do
programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''
from time import sleep

lista_consumo = []                  # Lista para armazenar as listas de veículos e a de lista de consumo
i = j = 0
combustivel = 2.25
distancia = 1000

# Preenche as listas lista_veiculo, lista_consumo_veiculo e lista_consumo
for veiculo in range(0, 5):
    lista_veiculo = []              # Lista para cadastro somente dos veículos
    lista_consumo_veiculo = []      # Lista para cadastro do consumo de litros por veículos

    carro = str(input(f'Informe o nome do {veiculo + 1} veículo: ')).strip().upper()
    km_por_litro_str = str(input('KM por litro: ')).replace(',', '.')
    km_por_litro = float(km_por_litro_str)

    lista_veiculo.append(carro)
    lista_consumo_veiculo.append(lista_veiculo)
    lista_consumo_veiculo.append(km_por_litro)
    lista_consumo.append(lista_consumo_veiculo)

# Imprime o comparativo dos veículos
print(f'-' * 57)
print(' ' * 9, 'COMPARATIVO DE CONSUMO DE COMBUSTÍVEL')
print(f'-' * 57)
for lista in lista_consumo:
    print(f'Veículo: {i + 1}')
    print(f'Nome: {lista[0][0]}\nKm por litro: {lista[1]:.2f}')
    i += 1
print('')

# Imprime o relatório dos veículos
print('CRIANDO O RELATÓRIO DE CONSUMO DOS VEÍCULOS.....')
print('-' * 20, 'RELATÓRIO FINAL', '-' * 20)
sleep(1)
for resultado in lista_consumo:
    litro = distancia / resultado[1]
    custo = litro * combustivel
    sleep(0.75)
    print(f'{j + 1} - {resultado[0][0]}\t\t-\t\t {resultado[1]:.2f}\t\t-\t\t {litro:.2f} litros - R$ {custo:.2f}')
    j += 1
print(f'-' * 57)
print('FIM DO RELATÓRIO!')
