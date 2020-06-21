'''
16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até
que o valor seja maior que 500.
'''
ultimo = 1
penultimo = 1
print(ultimo, end=' ')
print(penultimo, end=' ')
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo, end=' ')
    else:
        print('\nO proximo valor será maior do que 500')