'''
6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro.
'''
print('Imprime os números de 1 a 20 um abaixo do outro.')
for num in range(1, 21):
    print(num)

print('Imprime os números de 1 a 20 um ao lado do outro.')
for num in range(1, 21):
    print(num, '-', end='')
