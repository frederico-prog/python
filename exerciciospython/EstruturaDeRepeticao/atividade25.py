'''
25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.
'''
soma = media = count = 0

while True:
    idade = int(input('Informe a sua idade: '))
    soma += idade
    count += 1
    media = soma / count
    if media == 0 or media <= 25:
        print('A turma é jovem!')
    resp = ' '
    sair = False
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N]')).upper().split()[0]
        if resp == 'N':
            sair = True
    if sair:
        break