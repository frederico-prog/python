# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
print('******** DESAFIO - AULA 07 - ANTECESSOR E SUCESSOR *********')
n1 = int(input('Digite um número: '))
ant = n1 - 1
suc = n1 + 1
print('O antecessor do número {0} é: {1}. E o seu sucessor é {2}.'.format(n1, ant, suc))
