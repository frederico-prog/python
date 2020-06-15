'''
CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UM LISTA. DEPOIS, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER PARES
E OS VALORES ÍMPARES DIGITADOS RESPECTIVAMENTE. AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.
'''
from time import sleep
valores = []
impar = []
par = []

while True:
    valor = int(input('Digite um valor: '))

    valores.append(valor)

    resp = str(input('Digite "C" para continuar e "S" para sair.')).upper().strip()[0]
    while resp not in 'CS':
        resp = str(input('Digite "C" para continuar e "S" para sair.')).upper().strip()[0]
    if resp == 'S':
        break

print('Criando as listas PAR e ÍMPAR...')
sleep(2)

for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista digitada foi: {valores}')
print(f'A lista de números PARES foi criada com os seguintes números: {par}')
print(f'A lista de números ÍMPARES foi criada com os seguintes números: {impar}')
