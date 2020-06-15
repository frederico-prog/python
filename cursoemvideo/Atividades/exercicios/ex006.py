# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
print('******** DESAFIO - AULA 07 - CALCULADORA *********')
n1 = int(input('Digite um valor: '))
d = n1 * 2
t = n1 * 3
#r = n1 ** (1/2)
r = pow(n1, (1/2))
print('O dobro do número {} é {}. \nO seu triplo é {} e a sua raiz quadrada é {:.2f}'.format(n1, d, t, r))
