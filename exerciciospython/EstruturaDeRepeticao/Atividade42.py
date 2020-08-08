'''
42 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número
negativo.
'''
import random
from time import sleep

count_intervalo_025 = count_intervalo_2650 = count_intervalo_5175 = count_intervalo_76100 = total_numero = 0

while True:
    numero = random.randint(-5, 100)

    sleep(1)

    if 0 <= numero <= 25:
        print(f'O número {numero} está no intervalo de [0-25].')
        count_intervalo_025 += 1
    if 26 < numero <= 50:
        print(f'O número {numero} está no intervalo de [26-50].')
        count_intervalo_2650 += 1
    if 51 < numero <= 75:
        print(f'O número {numero} está no intervalo de [51-75].')
        count_intervalo_5175 += 1
    if 76 < numero <= 100:
        print(f'O número {numero} está no intervalo de [76-100].')
        count_intervalo_76100 += 1
    if numero < 0:
        print(f'Número {numero} tem o valor negativo. Saindo do sistema.')
        break

total_numero = count_intervalo_025 + count_intervalo_2650 + count_intervalo_5175 + count_intervalo_76100

print(f'Total de números gerados: {total_numero}')
print('')
print(f'Total de números por intervalos:\n[0-25] = {count_intervalo_025}\n[26-50] = {count_intervalo_2650}\n'
       f'[51-75] = {count_intervalo_5175}\n[76-100] = {count_intervalo_76100}')
