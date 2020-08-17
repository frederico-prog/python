'''
22 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
    a - necessita da esfera;
    b - necessita de limpeza;
    c - necessita troca do cabo ou conector;
    d - quebrado ou inutilizado
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''
tipo_manutencao = (
    'necessita da esfera',
    'necessita de limpeza',
    'necessita troca do cabo ou conector',
    'quebrado ou inutilizado'
)
lista_defeito = []
i = total_mouse = 0
id_mouse = -1

for situacao in tipo_manutencao:
    print(f'{i + 1} - {situacao.upper()}')
    i += 1

while id_mouse != 0:
    id_mouse = int(input('Informe o id do mouse ou 0 para sair: '))
    if id_mouse == 0:
        print('Cadastro da situação dos mouses realizada com sucesso.')
        break
    else:
        lista_mouse = []
        total = 0
        cod_manutencao = int(input('Informe o código para a manutenção do mouse: '))
        lista_mouse.append(id_mouse)
        lista_mouse.append(cod_manutencao)
        lista_defeito.append(total)
        lista_defeito.append(lista_mouse)
        total_mouse += 1
print(lista_defeito)
print(f'Quantidade de mouses: {total_mouse}')

print('\t\tSituação\t\t\t\t\tQuantidade\t\t\t\tPercentual')
for key, value in enumerate(lista_defeito):
    texto = tipo_manutencao[key - 1]
    print(f'{texto.upper()}')
