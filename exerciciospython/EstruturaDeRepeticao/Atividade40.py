'''
40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
    a - Código da cidade;
    b - Número de veículos de passeio (em 1999);
    c - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    d - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    e - Qual a média de veículos nas cinco cidades juntas;
    e - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
from datetime import datetime
from time import sleep

ano = datetime.now()
print('-=-' * 20)
print('{:^60}'.format(f'SENSO DE ACIDENTES {ano.year}'))
print('-=-' * 20)

dados = {}
lista_senso = []
maior_indice = menor_indice = media_veiculo = media_acidente = soma_acidente = soma_veiculo = count = 0


while True:
    dados.clear()
    count += 1
    estado = str(input('Informe o Estado: ')).upper()
    cidade = str(input('Informe o nome da cidade: ')).capitalize().strip()
    print('Caso deseje consultar o código da cidade clique no link https://cidades.ibge.gov.br')
    cod_cidade = int(input('Informe o código IBGE da cidade: '))
    num_habitante = int(input(f'Informe o número de habitantes na cidade {cidade}: '))
    num_veiculo = int(input(f'Número de veículos em {ano.year}: '))
    num_acidente = int(input(f'Informe o número de acidentes no ano de {ano.year}: '))
    dados['estado'] = estado
    dados['cidade'] = cidade
    dados['cod_cidade'] = cod_cidade
    dados['num_habitante'] = num_habitante
    dados['num_veiculo'] = num_veiculo
    dados['ano'] = ano.year
    dados['num_acidente'] = num_acidente
    soma_veiculo += dados['num_veiculo']

    lista_senso.append(dados.copy())

    # Verifica o número de habitantes e soma o total de acidentes
    if dados['num_habitante'] <= 2000:
        soma_acidente += dados['num_acidente']

    # Verifica o menor e o maior indice de acidentes
    if count == 1:
        maior_indice = menor_indice = dados['num_acidente']
    else:
        if dados['num_acidente'] > maior_indice:
            maior_indice = dados['num_acidente']
        if dados['num_acidente'] < menor_indice:
            menor_indice = dados['num_acidente']

    # Verifica a resposta do usuário
    resposta = str(input('Deseja inserir uma nova cidade? "C" para continuar ou "S" para sair: ')).upper()[0]

    while resposta not in 'CS':
        resposta = str(input('Deseja inserir uma nova cidade? "C" para continuar ou "S" para sair: ')).upper()[0]

    if resposta == 'S':
        break

# Imprimindo o resultado da pesquisa
print('VERIFICANDO RESULTADO....')
sleep(1)
print('RESULTADO DA PESQUISA!')
for cidade in lista_senso:
    if cidade['num_acidente'] == maior_indice:
        print(f'CIDADE COM O MAIOR INDICE DE ACIDENTES EM {ano.year}')
        print(f'Cidade: {cidade["cidade"]}-{cidade["estado"]}\nCódigo IBGE: {cidade["cod_cidade"]}\n'
              f'Maior indice: {maior_indice}')
    if cidade['num_acidente'] == menor_indice:
        print(f'CIDADE COM O MENOR INDICE DE ACIDENTES EM {ano.year}')
        print(f'Cidade: {cidade["cidade"]}-{cidade["estado"]}\nCódigo IBGE: {cidade["cod_cidade"]}\n'
              f'Menor indice: {menor_indice}')

media_veiculo = soma_veiculo / len(lista_senso)
media_acidente = soma_acidente / len(lista_senso)

print(f'Medias Acidentes por 2000 habitantes: {media_acidente}\nMédia de veículos em {ano.year}: {media_veiculo}')
