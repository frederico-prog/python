# O mesmo professor do desafio anterior quer sotear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
print('******** DESAFIO - AULA 08 - ORDEM DE APRESENTAÇÃO *********')
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)

print('Ordem de apresentação:')
print(lista)
