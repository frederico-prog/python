# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma parede de 2m².
print('******** DESAFIO - AULA 07 - CALCULADORA 4 *********')
n1 = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede: '))
# metro = 2
area = n1 * n2
total = area / 2
print('Para uma área de {:.3f}m². \nSerão necessárias a utilização de {:.4f}l de tintas.'.format(area, total))
