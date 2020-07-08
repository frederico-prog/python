'''
18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
print('-=-' * 20)
print('{:^60}'.format(' TRATANDO VÁRIOS VALORES 2 - v1.0 '))
print('-=-' * 20)

count = maior = menor = soma = 0
resp = 'S'

while resp in 'Ss':
    num = int(input('Informe o número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = soma = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? Digite S para continuar e N para parar: ')).upper().strip()[0]

print(f'Foram digitado {count} números.')
print(f'O maior número é o {maior} e o menor é {menor}.')
print(f'A soma dos números digitados foi: {soma}')
