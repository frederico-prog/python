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
idMouse = -1
defeitos = ('1 - Necessita de Esfera',
            '2 - Necessita de limpeza',
            '3 - Necessita troca de cabo ou conector',
            '4 - Quebrado ou inutilizado')
totalDefeitos = [0] * 4
totalMouses = 0

for i in defeitos:
    print('%s' % i)

while idMouse != 0:
    idMouse = int(input('Identificador do Mouse: '))
    if idMouse != 0:
        defeito = int(input('Codigo do defeito: '))
        totalDefeitos[defeito - 1] += 1
        totalMouses += 1

print('Quantidade de mouses: %d ' % totalMouses)

print('Situacao\tQuantidade\tPercentual')
for i in range(0, len(defeitos)):
    print('%s\t%d\t%.2f' % (defeitos[i], totalDefeitos[i], totalDefeitos[i] / float(totalMouses) * 100))
