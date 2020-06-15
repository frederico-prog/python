# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
print('******** DESAFIO - AULA 08 - CALCULAR SENO, COSENO E A TANGENTE *********')
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja calcular: '))
seno = sin(radians(ângulo))
cos = cos(radians(ângulo))
tg = tan(radians(ângulo))
print('O ângulo de {}° tem: \nSeno = {:.2f}°. \nCoseno = {:.2f}°. \nTangente = {:.2f}°.'.format(ângulo, seno, cos, tg))
