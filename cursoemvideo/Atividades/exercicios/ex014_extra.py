# Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, cm, dm, mm
print('******** DESAFIO - AULA 07 - CONVERSÃO 2 *********')
m = float(input('Digite o valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('Quilômetro: {:.2f}km. \nHectômetro: {:.2f}hm. \nDecâmetro: {:.2f}dam. \nMetro: {:.2f}m. \nCentímetro: {:.2f}cm.'
      '\nDecímetro: {:.2f}dm. \nMilímetro: {:.2f}mm'.format(km, hm, dam, m, dam, cm, mm))
