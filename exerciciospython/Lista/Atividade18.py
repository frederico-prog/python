'''
18 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a
linguagem de programação Python. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente
ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido
for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o
final da votação, o programa deverá exibir:
    a - O total de votos computados;
    b - Os númeos e respectivos votos de todos os jogadores que receberam votos;
    c - O percentual de votos de cada um destes jogadores;
    d - O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual
    de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada
jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das
informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no
disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''
from time import sleep
import collections
import operator

num_jogador = -1
lista_jogador = []
total_votos = melhor_jogador = 0

# Preenche a lista com o voto dos jogadores
print('Enquete: Quem foi o melhor jogador?\n')
print('Informe um valor entre 1 e 23 ou 0 para sair!\n')
while num_jogador != 0:
    num_jogador = int(input('Número do jogador (0=fim): '))

    # Verifica se o valor digitado é menor que 0 ou maior que 23
    if num_jogador < 0 or num_jogador > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        continue

    # Verifica se o valor digitado está entre 1 e 23
    if 0 < num_jogador <= 23:
        lista_jogador.append(num_jogador)
        total_votos += 1

    if num_jogador == 0:
        print('INSERÇÃO DE DADOS DA PESQUISA FINALIZADO!')
        break
print('CALCULANDO OS RESULTADOS.....')
sleep(1)
print('Resultado da votação.\n')
print(f'Foram computados {total_votos} votos.\n')

# Verifica qual foi o jogador que recebeu o maior número de votação
votos = collections.Counter(lista_jogador)
melhor_jogador = max(votos.items(), key=operator.itemgetter(1))

# Imprime a lista de votos dos jogadores
print('JOGADOR\t\tVOTO\t\t%')
for key, value in votos.items():
    sleep(0.75)
    print(f'{key}\t\t\t{value}\t\t\t{value / total_votos * 100}%')

# Imprime o melhor jogador e a quantide de votos que ele recebeu
print(f'O melhor jogador foi o {melhor_jogador[0]} com {melhor_jogador[1]} votos.\n')

print('PESQUISA FINALIZADA COM SUCESSO.')
