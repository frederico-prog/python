# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
print('******** DESAFIO - AULA 07 - CALCULADORA 6 *********')
nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o valor do salário do funcionário: R$ '))
novosal = salario + (salario * 15 / 100)
print('O funcionário {} passará a receber o salário de R${:.2f} recebendo 15% de aumento.'.format(nome, novosal))
