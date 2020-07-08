'''
20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
'''
resp = 'S'

while resp in 'Ss':
    ultimo = 1
    penultimo = 1
    print(ultimo, end=' ')
    print(penultimo, end=' ')
    termo = 0
    while termo < 16:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if termo < 16:
            print(termo, end=' ')
        else:
            print('\nO proximo valor será maior do que 16')
    resp = str(input('Deseja continuar? Digite S para continuar e N para parar: ')).upper().strip()[0]
print('FIM DA EXECUÇÃO DO PROGRAMA!')