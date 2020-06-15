# def soma(num1, num2):
#     resp = num1 + num2
#     return resp
#
# retorno = soma(12345.99, 5678.02)
# print(retorno)

# def imprime_oi():
#     print('OI')
#
# imprime_oi()

# FUNÇÃO - POSSUI RETORNO
# MÉTODO - NÃO POSSUI RETORNO
# def tem_sete_itens(argumento):
#     if len(argumento) == 7:
#         return True
#     else:
#         return False
#
#
# if tem_sete_itens('12345678'):
#     print('Realmente o tamanho é 7')
# else:
#     print('O tamanho não é igual a sete')


'''
EXERCÍCIO:
Escreva uma função que receba um objeto de coleção e retorna o valor do maior número dentro dessa coleção.
Escreva uma outra função que retorne o menor valor desta coleção.
'''
import random


def maior_menor(colecao):
    for num in colecao:
        maior = max(num)
        menor = min(num)
    return print('O maior número é o {} e o menor é o {}'.format(maior, menor))


#Cria uma lista vazia
lista_numeros = []

#Cria uma coleção de números aleatórios e adiciona na lista
aleatorio = random.sample(range(0, 100), 20)
lista_numeros.append(aleatorio)

#Imprime a lista criada
print('Lista de números: ', lista_numeros)

#Chama a função que verifica o maior e o menor valor da coleção
maior_menor(lista_numeros)

