# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.
print('******** DESAFIO - AULA 06B *********')
variavel = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é: ', type(variavel))
print('Só tem espaço? ', variavel.isspace())
print('É um número? ', variavel.isnumeric())
print('É alfabético? ', variavel.isalpha())
print('É alfanumérico? ', variavel.isalnum())
print('Está em maiúscula? ', variavel.isupper())
print('Está em minúscula? ', variavel.islower())
print('Está capitalizada? ', variavel.istitle())
