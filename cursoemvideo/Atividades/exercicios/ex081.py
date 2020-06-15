'''
CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA. DEPOIS, MOSTRE:
A- QUANTOS NÚMEROS FORAM DIGITADOS.
B- A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
C- SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.
'''
valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Digite "C" para continuar ou "S" para sair')).strip().upper()[0]
    while resp not in 'CS':
        resp = str(input('Digite "C" para continuar ou "S" para sair')).strip().upper()[0]
    if resp in 'S':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 not in valores:
    print('O valor 5 não faz parte da lista.')
else:
    resultado = valores.count(5)
    print(f'O número 5 faz parte da lista. Ele aparece {resultado} vezes em sua lista.')
